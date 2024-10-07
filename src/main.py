#!/usr/bin/env python3
import json
from time import time
from typing import Any, Dict, List, TypeVar, Generic
from dataclasses import dataclass
from uuid import uuid4


@dataclass
class Job:
    execution_date: float

    @property
    def priority(self):
        return self.execution_date

    def __post_init__(self):
        self.id: str = str(uuid4())
        self.__dict__["id"] = self.id

    def to_dict(self) -> Dict[str, Any]:
        return self.__dict__
    
    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


T = TypeVar("T")
class PriorityQueue(Generic[T]):
    def __init__(self):
        self._items: List[T] = []

    @property
    def items(self) -> List[T]:
        return self._items
    
    def enqueue(self, item: T) -> None:
        if self.is_empty():
            self._items.append(item)
        else:
            for index, _item in enumerate(self._items):
                if item.priority > _item.priority:
                    self._items.insert(index, item)
    
    def dequeue(self) -> T:
        return self._items.pop(0)
    
    def delete(self, index: int) -> T:
        return self._items.pop(index)
    
    def peek(self) -> T:
        return self._items[0]
    
    def is_empty(self) -> bool:
        return (len(self._items) == 0)
    
    def size(self) -> int:
        return len(self._items)


class JobScheduler:
    def __init__(self):
        self._jobs: PriorityQueue[Job] = PriorityQueue()

    def schedule_job(self, execution_date: float) -> Job:
        job: Job = Job(
            execution_date=execution_date
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


def main():
    job_scheduler: JobScheduler = JobScheduler()
    job: Job = job_scheduler.schedule_job(execution_date=time())
    print(f"Scheduled the following job:\n{job}")
    jobs: List[Job] = job_scheduler.list_jobs()
    print(f"Current jobs:\n{json.dumps([job.to_dict() for job in jobs], indent=4)}")
    job = job_scheduler.get_job(job.id)
    print(f"Found the following job:\n{job}")
    job = job_scheduler.delete_job(job.id)
    print(f"Deleted the following job:\n{job}")
    jobs = job_scheduler.list_jobs()
    print(f"Current jobs:\n{json.dumps([job.to_dict() for job in jobs], indent=4)}")


if __name__ == "__main__":
    main()
