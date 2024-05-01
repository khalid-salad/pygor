#!/usr/bin/env python3

import math
from typing import Literal

from binary_heap import BinaryHeap
from graph_helper import (DirectedGraph, Edge, ImplicitTree, Node,
                          UndirectedGraph)


def dijkstras(graph: UndirectedGraph | DirectedGraph, root: Node) -> tuple[dict[Node, int | float], ImplicitTree]:
    n = len(graph.nodes)
    distance_from_root: dict[Node, int | float] = {node: math.inf for node in graph.nodes}
    parent: ImplicitTree = {node: None for node in graph.nodes}
    heap = BinaryHeap()
    distance_from_root[root] = 0
    heap.push(key=root, val=distance_from_root[root])

    already_popped: set[Node] = set()
    while len(heap) > 0 and len(already_popped) < n:
        next_closest = heap.pop()
        already_popped.add(next_closest)
        for edge in graph.edges_incident_on(next_closest):
            if edge.destination not in already_popped:
                old_dist = distance_from_root[edge.destination]
                new_dist = distance_from_root[next_closest] + edge.weight
                if new_dist < old_dist:
                    distance_from_root[edge.destination] = new_dist
                    parent[edge.destination] = next_closest
                    heap.push(key=edge.destination, val=new_dist)
    return distance_from_root, parent

def main() -> Literal[0]:
    return 0


if __name__ == "__main__":
    main()
