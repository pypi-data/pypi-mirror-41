"""
    crython/tab
    ~~~~~~~~~~~

    Contains functionality for executing jobs (python functions) from cron expressions.
"""
#  pylint: disable=global-statement, invalid-name
from __future__ import unicode_literals

import datetime
import threading
import multiprocessing
import time

from . import log
import logging
logger = logging.getLogger(__name__)


__all__ = ['CronTab', 'default_tab', 'start', 'stop']


#: Mapping of supported execution contexts for registered jobs.
EXECUTION_CONTEXTS = {
    'thread': lambda job, params: threading.Thread(target=job, kwargs = params).start(),
    'multiprocess': lambda job, params: multiprocessing.Process(target=job, kwargs = params).start(),
}

#: Default execution context to use if caller does not specify one.
DEFAULT_EXECUTION_CONTEXT = 'thread'


class CronTab(threading.Thread):
    """
    Background thread responsible for executing background jobs.
    """

    def __init__(self, *args, **kwargs):
        super(CronTab, self).__init__()
        self.name = 'CronTab ({0})'.format(kwargs.get('name', id(self)))
        self.daemon = True
        self.jobs = {}
        self.crons = {}
        self.params = {}
        self.jobs_lock = threading.RLock()
        self.proc_event = threading.Event()
        self.stop_event = threading.Event()

    def register(self, name, job):
        """
        Register the given name and function.

        :param name: Name of the registered job. **Note:** This should be unique.
        :param job: Callable decorated with :func:`~crython.job.job` to execute.
        :return: `None`.
        """
        with self.jobs_lock:
            self.jobs[name] = job
            self.crons[name] = job.cron_expression
            self.params[name] = job.params
            self.proc_event.set()

    def deregister(self, name):
        """
        De-register the job that was registered with the given name.

        :param name: Name of the job to remove.
        :return: `None`.
        """
        with self.jobs_lock:
            if name in self.jobs:
                del self.jobs[name]
                del self.crons[name]
                del self.params[name]
                if not self.jobs:
                    self.proc_event.clear()

    def stop(self):
        """
        Stop this background thread from executing any more jobs.

        :return: `None`.
        """
        with self.jobs_lock:
            self.stop_event.set()
            self.proc_event.clear()
            self.jobs.clear()
            self.crons.clear()
            self.params.clear()

    def run(self):
        """
        Background function that processes all registered jobs and invokes them based on their context and expression.
        """
        logger.info('{0} started'.format(self.name))
        try:
            # Wait until there is at least one registered job. No point is spinning otherwise.
            self.proc_event.wait()

            # Pop and execute any jobs that should be run at "reboot". Reboot, in this context, is just whenever
            # the executor starts running.

            #for job in (self.jobs.pop(k) for (k, v) in list(self.jobs.items()) if v.cron_expression.is_reboot):
            #    EXECUTION_CONTEXTS[job.ctx](job)

            #for (name, job) in list(self.jobs.items()):
            #    if self.crons[name].is_reboot:
            #        EXECUTION_CONTEXTS[job.ctx](job, self.params[name])
            #        self.deregister(name)

            # Spin loop.
            # TODO - This can be infinitely more efficient if we convert cron expressions to a
            # datetime/timedelta so we know exactly how long we should sleep before waking up to execute.
            while True:
                self.proc_event.wait()
                if self.stop_event.is_set():
                    logger.info('{0} stopped'.format(self.name))
                    break

                # Snapshot the current time and check all registered jobs to see if they "match". If so, we should
                # execute them immediately.
                now = datetime.datetime.now()
                #for job in self.jobs.copy().values():
                #    if job.cron_expression.matches(now):
                #        print (job.ctx, job.name)
                #        EXECUTION_CONTEXTS[job.ctx](job)

                for name, job in self.jobs.copy().items():
                    if self.crons[name].is_reboot:
                        EXECUTION_CONTEXTS[job.ctx](job, self.params[name])
                        self.deregister(name)

                    elif self.crons[name].matches(now):
                        EXECUTION_CONTEXTS[job.ctx](job, self.params[name])

                time.sleep(1)
        except Exception:  # pylint: disable=broad-except
            logger.exception('{0} encountered unhandled exception'.format(self.name))
        finally:
            logger.info('{0} exiting'.format(self.name))


#: The default, global tab instance that is created on import. This is the instance that will be used unless
#: the :func:`~crython.job.job` caller overrides it.
default_tab = CronTab(name='default')


def start():
    """
    Start the default, global :class:`~crython.tab.CronTab` instance.
    """
    global default_tab

    default_tab.start()


def stop():
    """
    Stop the default, global :class:`~crython.tab.CronTab` instance.

    This informs the background thread to stop processing new jobs but does not wait for it to
    finish completing its current ones. If the caller wishes to wait for the thread to stop completely,
    it should call :func:`join`.
    """
    global default_tab

    default_tab.stop()


def join(timeout=None):
    """
    Join the default, global :class:`~crython.tab.CronTab` instance thread.

    :param timeout: Timeout in seconds to block waiting on the crontab instance. If None, wait forever.
    """
    global default_tab

    return default_tab.join(timeout)
