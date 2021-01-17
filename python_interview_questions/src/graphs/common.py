import abc
import typing
from dataclasses import dataclass


@dataclass(frozen=True)
class WeightedConnection:
    value: int
    weight: int = 1

    def __str__(self):
        "WC({}, {})".format(self.value, self.weight)


class AbstractGraph(metaclass=abc.ABCMeta):
    """
    Abstract class representing graph structure.

    Consider nodes to be integers, because they could be mapped into any data.
    """
    @property
    @abc.abstractmethod
    def directed(self):
        pass

    @abc.abstractmethod
    def add_vertex(self, v: int):
        pass

    @abc.abstractmethod
    def remove_vertex(self, v: int):
        pass

    @abc.abstractmethod
    def add_edge(self, u: int, v: int, weight: int = 1):
        pass

    @abc.abstractmethod
    def remove_edge(self, u: int, v: int):
        pass

    @abc.abstractmethod
    def neighbours(self, v: int) -> typing.Iterable[WeightedConnection]:
        pass

    @abc.abstractmethod
    def min_weight(self, u: int, v: int):
        pass


class AdjacencyMatrix(AbstractGraph):
    """
    Better for small graphs and graphs which are almost fully connected.

    Does not allow multiple edges between two vertices.
    """

    def __init__(self, number_of_vertices, weighted_edges, directed):
        self._number_of_vertices = number_of_vertices
        self._directed = directed
        self._matrix = [[0 for _ in range(number_of_vertices)] for _ in range(number_of_vertices)]
        for i, j, weight in weighted_edges:
            self._matrix[i][j] = weight
            if not directed:
                self._matrix[j][i] = weight

    @property
    def directed(self):
        return self._directed

    def add_edge(self, u: int, v: int, weight: int = 1):
        self._matrix[u][v] = weight

    def remove_edge(self, u: int, v: int):
        self._matrix[u][v] = 0

    def add_vertex(self, v: int):
        raise NotImplementedError("AdjacencyMatrix does not support adding vertices")

    def remove_vertex(self, v: int):
        raise NotImplementedError("AdjacencyMatrix does not support removing vertices")

    def neighbours(self, v):
        return (
            WeightedConnection(i, self._matrix[v][i])
            for i in range(self._number_of_vertices) if self._matrix[v][i]
        )

    def min_weight(self, u: int, v: int):
        return self._matrix[u][v]

    def __str__(self):
        return "\n".join([
            " ".join([str(self._matrix[i][j]) for j in range(self._number_of_vertices)])
            for i in range(self._number_of_vertices)
        ])


class AdjacencySet(AbstractGraph):
    """
    Better for big graphs with not so big number of edges.

    Allow multiple edges with different weights between two vertices.
    """

    def __init__(self, vertices, weighted_edges, directed):
        self._graph = {}
        self._directed = directed
        for v in vertices:
            self.add_vertex(v)
        for i, j, weight in weighted_edges:
            self.add_edge(i, j, weight)

    @property
    def directed(self):
        return self._directed

    def add_vertex(self, v: int):
        self._graph.setdefault(v, set())

    def add_edge(self, u: int, v: int, weight: int = 1):
        self._graph.setdefault(u, set()).add(WeightedConnection(v, weight))
        if not self._directed:
            self._graph.setdefault(v, set()).add(WeightedConnection(u, weight))

    def remove_vertex(self, v: int):
        if v in self._graph:
            del self._graph[v]
        for i in list(self._graph.keys()):
            has_connections_with_v = any(wc.value == v for wc in self._graph[i])
            if has_connections_with_v:
                self._graph[i] = {wc for wc in self._graph[i] if wc.value != v}

    def remove_edge(self, u: int, v: int):
        self._graph[u] = {wc for wc in self._graph[u] if wc.value != v}
        if not self._directed:
            self._graph[v] = {wc for wc in self._graph[v] if wc.value != u}

    def min_weight(self, u: int, v: int):
        all_weights = [wc.weight for wc in self._graph[u] if wc.value == v]
        if len(all_weights) == 0:
            return 0
        elif len(all_weights) == 1:
            return all_weights[0]
        return min(*all_weights)

    def neighbours(self, v):
        return (i for i in self._graph[v])

    def __str__(self):
        return "\n".join("{}: {}".format(i, wc) for i, wc in self._graph.items())
