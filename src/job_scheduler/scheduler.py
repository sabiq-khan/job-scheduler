from time import time
from typing import Callable, List
from job_scheduler.job import Job
from job_scheduler.priority_queue import PriorityQueue
from threading import Timer


class JobScheduler:
    def __init__(self):
        self._jobs: PriorityQueue[Job] = PriorityQueue()

    def schedule_job(self, execution_date: float, task: Callable) -> Job:
        job: Job = Job(
            execution_date=execution_date,
            task=task
        )
        self._jobs.enqueue(job)

        return job
    
    def get_job(self, id: str) -> Job:
        for job in self._jobs.items:
            if job.id == id:
                return job
        
        raise ValueError(f"Job '{id}' not found.")
    
    def list_jobs(self) -> List[Job]:
        return self._jobs.items
    
    def delete_job(self, id: str) -> Job:
        for index, job in enumerate(self._jobs.items):
            if job.id == id:
                self._jobs.delete(index)
                return job
        
        raise ValueError(f"Job '{id}' not found.")
