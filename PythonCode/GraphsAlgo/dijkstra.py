import sys
# import heapq


class DijkstraPath(object):
    def __init__(self, g):
        self.my_graph = g
        self.vertex_marks = [0 for _ in range(g.n_vertex)]
        self.path_found = None
    
    def find_path(self, vertex_1, vertex_2):
        print("Begin to find path")
        marked = [False for _ in range(self.my_graph.n_vertex)]
        distances = [sys.maxsize for _ in range(self.my_graph.n_vertex)]
        distances[vertex_1] = 0
        marked[vertex_1] = True
        while not all(marked):
            curr_min_dist = sys.maxsize
            curr_min_vertex = vertex_1
            for i, k in enumerate(distances):
                if not marked[i] and curr_min_dist > k:
                    curr_min_dist = k
                    curr_min_vertex = i
            print("Curr min: {}".format(curr_min_vertex))
            marked[curr_min_vertex] = True
            for v in self.my_graph.neighbours(curr_min_vertex):
                if not marked[v]:
                    distances[v] = min(distances[v], distances[curr_min_vertex] + self.my_graph.weight(curr_min_vertex, v))
                    
        print("Min distance [{}, {}]: {}".format(vertex_1, vertex_2, distances[vertex_2]))


if __name__ == "__main__":
    import graph
    print("Example 2:")
    dijkstra_m_2 = DijkstraPath(graph.adj_m_2)
    dijkstra_m_2.find_path(0, 4)
