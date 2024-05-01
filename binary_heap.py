#!/usr/bin/env python3

import heapq
from dataclasses import dataclass, field
from typing import Any, ClassVar, Literal


@dataclass
class keyvalpair:
    key: Any
    val: Any
    
    def __lt__(self, other):
        return self.val < other.val or self.val == other.val and self.key < other.key

@dataclass
class BinaryHeap:
    __heap: list[keyvalpair] = field(default_factory=list)
    is_max_heap: bool = False
    __multiplier: Literal[1] | Literal[-1] = -1 if is_max_heap else 1

    def push(self, *, key: Any, val: Any) -> None:
        heapq.heappush(self.__heap, keyvalpair(self.__multiplier * key, val))

    def top(self) -> Any:
        try:
            return self.__heap[0].key
        except IndexError:
            raise "Heap is empty."

    def pop(self) -> Any:
        try:
            return heapq.heappop(self.__heap).key
        except IndexError:
            raise "Heap is empty."

    def pushpop(self, *, key: Any, val: Any) -> Any:
        return heapq.heappushpop(self.__heap, keyvalpair(self.multiplier * key, val))
    
    def poppush(self, *, key: Any, val: Any) -> Any:
        try:
            return heapq.heapreplace(self.__heap, keyvalpair(self.multiplier * key, val))
        except IndexError:
            raise "Heap is empty."

    def __len__(self) -> int:
        return len(self.__heap)

    def __getitem__(self, index):
        assert index == 0
        return self.top()

def main() -> Literal[0]:
    return 0

    
if __name__ == "__main__":
    main()