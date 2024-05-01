#!/usr/bin/env python3

import math
from typing import Literal

from graph_helper import DirectedGraph, Edge, ImplicitTree, Node
from itertools import permutations


def bellman_ford(graph: DirectedGraph, root: Node) -> tuple[dict[Node, int | float], ImplicitTree]:
    n = len(graph.nodes)
    distance_from_root: dict[Node, int | float] = {v: math.inf for v in graph.nodes}
    parent: ImplicitTree = {v: None for v in graph.nodes}
    distance_from_root[root] = 0

    def update_distances() -> bool:
        update_occurred = False
        for edge in graph.edges:
            old_dist = distance_from_root[edge.destination]
            new_dist = distance_from_root[edge.source] + edge.weight
            if new_dist < old_dist:
                update_occurred = True
                distance_from_root[edge.destination] = new_dist
                parent[edge.destination] = edge.source
        return update_occurred

    print(distance_from_root)
    for _ in range(n - 1):
        update_occurred = update_distances()
        print(distance_from_root)
        if not update_occurred:  # no updates means we can terminate early
            return distance_from_root, parent

    update_occurred = update_distances()
    print(distance_from_root)
    print()
    if update_occurred:  # nth update means negative weight cycle
        print("negative weight cycle found")
        exit()
    return dist, parent


def main() -> Literal[0]:
    return 0


if __name__ == "__main__":
    main()
