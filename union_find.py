#!/usr/bin/env python3

from collections.abc import Hashable
from dataclasses import dataclass, field


class UnionFind:
    def __init__(self, *args:Hashable):
        self.parent = {arg: arg for arg in args}
        self.size = {arg: 1 for arg in args}
        self.number_of_subsets = len(args)


    def make_set(self, x:Hashable) -> None:
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1
            self.number_of_subsets += 1


    def is_root(self, x: Hashable) -> bool:
        return self.parent[x] == x


    def different_subsets(self, x: Hashable, y:Hashable) -> bool:
        return not self.same_subsets(x, y)


    def same_subsets(self, x: Hashable, y: Hashable) -> bool:
        return self.find(x) == self.find(y)


    def find(self, x: Hashable) -> Hashable:
        if not self.is_root(x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


    def union(self, x: Hashable, y: Hashable) -> None:
        if self.different_subsets(x, y):
            x = self.find(x)
            y = self.find(y)
            if self.size[x] < self.size[y]:
                x, y = y, x
            self.parent[y] = x
            self.size[x] += self.size[y]
            self.number_of_subsets -= 1
            
    def __str__(self) -> str:
        sets:dict[Hashable, set[Hashable]] = {x:set() for x in self.parent if self.is_root(x)}
        for x in self.parent:
            root = self.find(x)
            sets[root].add(x)
        result = ""
        for representative, subset in sets.items():
            result = f"{result}{representative}: {subset}\n"
        return result