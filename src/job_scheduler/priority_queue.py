from typing import List, TypeVar, Generic

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
