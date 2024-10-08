#!/usr/bin/env python3
import json
from time import sleep, time
from typing import List
from job_scheduler.tasks import goodbye, hello
from job_scheduler.job import Job
from job_scheduler.scheduler import JobScheduler


def main():
    job_scheduler: JobScheduler = JobScheduler()
    job: Job = job_scheduler.schedule_job(execution_date=(time() + 5), task=hello)
    print(f"Scheduled the following job:\n{job}")
    job = job_scheduler.schedule_job(execution_date=(time() + 25), task=goodbye)
    print(f"Scheduled the following job:\n{job}")
    jobs: List[Job] = job_scheduler.list_jobs()
    print(f"Current jobs:\n{json.dumps([job.to_json_encodable() for job in jobs], indent=4)}")
    job = job_scheduler.get_job(job.id)
    print(f"Found the following job:\n{job}")
    job = job_scheduler.delete_job(job.id)
    print(f"Deleted the following job:\n{job}")
    jobs = job_scheduler.list_jobs()
    print(f"Current jobs:\n{json.dumps([job.to_json_encodable() for job in jobs], indent=4)}")
    sleep(30)


if __name__ == "__main__":
    main()
