# import json


class Graph(object):
    _graph = None

    def __init__(self, f_path):
        with open(f_path) as f:
            is_oriented = "->" in f.readline()
            # print("oriented = {}".format(is_oriented))
            self.n_vertex, self.n_edge = map(int, f.readline().strip().split())
            self.vertex_pairs = {}
            for i in f.readlines():
                edge_info = [int(j) for j in i.strip().split()]
                self.vertex_pairs[(edge_info[0], edge_info[1])] = 1 if len(edge_info) == 2 else edge_info[2]
    
                # print("{}\n{}\n{}".format(self.n_vertex, self.n_edge, "\n".join([str(k) for k in self.vertex_pairs])))
            self.build_graph(self.vertex_pairs, is_oriented)

    def build_graph(self, vertex_pairs, is_oriented):
        raise NotImplementedError

    def neighbours(self, v):
        raise NotImplementedError

    def weight(self, u, v):
        return self.vertex_pairs[(u, v)]


class AdjacencyMatrix(Graph):
    """For small graphs"""

    def build_graph(self, vertex_pairs, is_oriented):
        self._graph = [[0 for _ in range(self.n_vertex)] for _ in range(self.n_vertex)]
        for i, j in vertex_pairs:
            self._graph[i][j] = 1
            if not is_oriented:
                self._graph[j][i] = 1
        # print(json.dumps(self._graph, indent=1))

    def neighbours(self, v):
        return (i for i in range(self.n_vertex) if self._graph[v][i])

    def __str__(self):
        return "\n".join([" ".join([str(self._graph[i][j]) for j in range(self.n_vertex)]) for i in range(self.n_vertex)])


class AdjacencySet(Graph):
    """For big graphs with not so big number of edges"""

    def build_graph(self, vertex_pairs, is_oriented):
        self._graph = [set() for _ in range(self.n_vertex)]
        for i, j in vertex_pairs:
            self._graph[i].add(j)
            if not is_oriented:
                self._graph[j].add(i)
        # print(json.dumps(self._graph, indent=1))

    def neighbours(self, v):
        return (i for i in self._graph[v])

    def __str__(self):
        return "\n".join([" ".join([str(i)] + [str(j) for j in self._graph[i]]) for i in range(self.n_vertex)])


adj_m_1 = AdjacencyMatrix("graph_example_1.txt")
adj_s_1 = AdjacencySet("graph_example_1.txt")
adj_m_2 = AdjacencyMatrix("graph_example_2.txt")
adj_s_2 = AdjacencySet("graph_example_2.txt")


if __name__ == "__main__":
    # import networkx as nx
    print("Example 1:")
    print("AdjacencyMatrix:\n" + str(adj_m_1))
    print("AdjacencySet:\n" + str(adj_s_1))
    print("Example 2:")
    print("AdjacencyMatrix:\n" + str(adj_m_2))
    print("AdjacencySet:\n" + str(adj_s_2))
    # print("Adjacency LIST:\n{}".format(adj_s_2._graph))
