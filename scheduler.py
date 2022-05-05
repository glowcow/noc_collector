#!/bin/python3

from express_poller import poller
from nd_backup import cfg_backup
from traceback import format_exc
from schedule import Scheduler
import datetime, time

class safe_scheduler(Scheduler):
    def __init__(self, reschedule_on_failure=True):
        self.reschedule_on_failure = reschedule_on_failure
        super().__init__()
    def _run_job(self, job):
        try:
            super()._run_job(job)
        except Exception:
            print(format_exc())
            job.last_run = datetime.datetime.now()
            job._schedule_next_run()

def main():
    scheduler = safe_scheduler()
    scheduler.every(10).minutes.do(poller.main) #express poller
    scheduler.every().day.at("02:30").do(cfg_backup.main) #configuration files backup from network devices
    while True:
        scheduler.run_pending()
        timestamp = time.strftime('%d-%b-%Y %H:%M:%S')
        print(f'{"="*10} all pending jobs are ran at {timestamp} {"="*10}')
        time.sleep(1)

if __name__ == "__main__":
    main()
