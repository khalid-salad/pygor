#!/usr/bin/env python3

from collections.abc import Hashable
from dataclasses import dataclass
from typing import Iterator, Sequence, TypeAlias

Node: TypeAlias = Hashable


@dataclass
class Edge:
    source: Node
    destination: Node
    weight: int | float = 1

    def __repr__(self) -> str:
        return f"({self.source}, {self.destination})"


class TraversalData:
    def __init__(self, nodes: Sequence[Node]):
        self.visited = {v: False for v in nodes}

    def mark_visited(self, node: Node) -> None:
        self.visited[node] = True

    def already_visited(self, node: Node) -> bool:
        return self.visited[node]

    def reset(self) -> None:
        self.visited = {v: False for v in self.visited.keys()}


class BaseGraph:
    def __init__(self, nodes: Sequence[Node], edges: Sequence[Edge]):
        self.nodes = list(nodes)
        self.edges = list(edges)


class UndirectedGraph(BaseGraph):
    def __init__(self, nodes: Sequence[Node], edges: Sequence[Edge]):
        super().__init__(nodes, edges)
        self.adj: dict[Node, set[Edge]] = {v: [] for v in self.nodes}
        for edge in edges:
            u, v, w = edge.source, edge.destination, edge.weight
            redge = Edge(v, u, w)
            self.adj[u].append(edge)
            self.adj[v].append(redge)

    def neighbors(self, node: Node) -> Iterator[Node]:
        yield from (edge.destination for edge in self.adj[node])

    def edges_incident_on(self, node: Node) -> Iterator[Edge]:
        yield from self.adj[node]


class DirectedGraph(BaseGraph):
    def __init__(self, nodes: Sequence[Node], edges: Sequence[Edge]):
        super().__init__(nodes, edges)
        self.out_adj: dict[Node, list[Edge]] = {v: [] for v in self.nodes}
        self.in_adj: dict[Node, list[Edge]] = {v: [] for v in self.nodes}
        self.rout_adj: dict[Node, list[Edge]] = {v: [] for v in self.nodes}
        self.rin_adj: dict[Node, list[Edge]] = {v: [] for v in self.nodes}
        for edge in edges:
            u, v, w = edge.source, edge.destination, edge.weight
            self.out_adj[u].append(edge)
            self.in_adj[v].append(edge)
            redge = Edge(v, u, -w)
            self.rout_adj[v].append(redge)
            self.rin_adj[u].append(redge)

    def neighbors(self, node: Node) -> Iterator[Node]:
        yield from (edge.destination for edge in self.out_adj[node])

    def in_neighbors(self, node: Node) -> Iterator[Node]:
        yield from (edge.destination for edge in self.in_adj[node])

    def edges_incident_on(self, node: Node) -> Iterator[Edge]:
        yield from self.out_adj[node]

    def in_edges_incident_on(self, node: Node) -> Iterator[Edge]:
        yield from self.in_adj[node]

    def reverse_edges(self) -> None:
        self.out_adj, self.rout_adj = self.rout_adj, self.out_adj
        self.in_adj, self.rin_adj = self.rin_adj, self.in_adj


class graph:
    def __init__(self, nodes, edges) -> None:
        pass

ImplicitTree = dict[Node, Node | None]
ExplicitTree = list[Edge]