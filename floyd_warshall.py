#!/usr/bin/env python3

import math
from typing import Literal
import itertools

from graph_helper import DirectedGraph, Edge, ImplicitTree, Node

def floyd_warshall(graph:DirectedGraph) -> dict[tuple[Node, Node], int | float]:
    distance: dict[tuple[Node, Node], int | float] = {(u, v): math.inf for u, v in itertools.product(graph.nodes, repeat=2)}
    for u in graph.nodes:
        distance[u, u] = 0
    for edge in graph.edges:
        distance[edge.source, edge.destination] = edge.weight
    for new_vertex in graph.nodes:
        for start in graph.nodes:
            for dest in graph.nodes:
                old_dist = distance[start, dest]
                new_dist = distance[start, new_vertex] + distance[new_vertex, dest]
                if new_dist < old_dist:
                    if start == dest:
                        print(f"graph has negative weight cycle at {start}")
                        exit()
                    else:
                        distance[start, dest] = new_dist

    return distance

def main() -> Literal[0]:
    return 0

if __name__ == "__main__":
    main()