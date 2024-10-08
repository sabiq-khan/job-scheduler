import json
from threading import Timer
from time import time
from typing import Any, Dict, Callable
from dataclasses import dataclass
from uuid import uuid4


@dataclass
class Job:
    execution_date: float
    task: Callable

    @property
    def priority(self):
        return self.execution_date

    def __post_init__(self):
        self.id: str = str(uuid4())
        self.__dict__["id"] = self.id

        self._execution: Timer = Timer(
            interval=(self.execution_date - time()),
            function=self.task
        )
        self._execution.start()

    def to_dict(self) -> Dict[str, Any]:
        return self.__dict__
    
    def to_json_encodable(self) -> Dict[str, Any]:
        json_encodable: Dict[str, Any] = {
            **self.to_dict(),
            "task": self.task.__name__,
        }
        json_encodable.pop("_execution")

        return json_encodable
    
    def __str__(self):
        return json.dumps(self.to_json_encodable(), indent=4)