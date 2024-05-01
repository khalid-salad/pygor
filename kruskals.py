#!/usr/bin/env python3

from typing import Literal

from graph_helper import DirectedGraph, Edge, ExplicitTree, UndirectedGraph
from union_find import UnionFind


def kruskals(graph:UndirectedGraph | DirectedGraph) -> ExplicitTree:
    uf = UnionFind(*graph.nodes)
    mst: ExplicitTree = []
    for edge in sorted(graph.edges, key=lambda edge: edge.weight):
        if uf.different_subsets(edge.source, edge.destination):
            uf.union(edge.source, edge.destination)
            mst.append(edge)
    return mst
    

def main() -> Literal[0]:
    return 0

if __name__ == "__main__":
    main()