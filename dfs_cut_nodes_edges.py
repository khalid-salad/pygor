#!/usr/bin/env python3

from typing import Literal

from graph_helper import Edge, Node, TraversalData, UndirectedGraph


def cut_vertices_and_edges(
    graph: UndirectedGraph,
) -> tuple[set[Node], list[Edge]]:
    trv = TraversalData(graph.nodes)
    dfsnum: dict[Node, int] = {v: 0 for v in graph.nodes}
    lownum: dict[Node, int] = {v: 0 for v in graph.nodes}
    parent_of: dict[Node, None | Node] = {v: None for v in graph.nodes}
    number_of_children_of: dict[Node, int] = {v: 0 for v in graph.nodes}
    cut_nodes: set[Node] = set()
    cut_edges: list[Edge] = []
    DFS_VISIT_ORDER = 0

    def is_tree_edge(edge: Edge) -> bool:
        return parent_of[edge.destination] == edge.source

    def is_back_edge(edge: Edge) -> bool:
        return parent_of[edge.source] == edge.destination
    
    def dfs(root: Node) -> None:
        trv.mark_visited(root)
        nonlocal DFS_VISIT_ORDER
        dfsnum[root] = lownum[root] = DFS_VISIT_ORDER
        DFS_VISIT_ORDER += 1
        for edge in graph.edges_incident_on(root):
            root, neighbor = edge.source, edge.destination
            if not trv.already_visited(neighbor):
                parent, child = root, neighbor
                parent_of[child] = parent
                number_of_children_of[parent] += 1
                dfs(child)
                lownum[parent] = min(lownum[parent], lownum[child])
                if lownum[child] > dfsnum[parent]: # edge is a cut edge
                    cut_nodes.add(parent)
                    cut_edges.append(edge)
                elif lownum[child] == dfsnum[parent]: # parent is a cut vertex if not root
                    cut_nodes.add(parent)
            elif is_back_edge(edge):
                lownum[root] = min(lownum[root], dfsnum[neighbor])

    for v in graph.nodes:
        if not trv.already_visited(v):
            dfs(v)
            if number_of_children_of[v] > 1:
                cut_nodes.add(v)
            else:
                cut_nodes.remove(v)

    return cut_nodes, cut_edges


def main() -> Literal[0]:
    return 0


if __name__ == "__main__":
    main()
