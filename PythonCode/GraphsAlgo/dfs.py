class DFSPath(object):
    def __init__(self, g):
        self.__my_graph = g
        self.vertex_marks = [0 for _ in range(g.n_vertex)]
        self.dfs_in = []
        self.dfs_out = []

    def reset(self, g):
        self.vertex_marks = [0] * len(self.vertex_marks)
        self.dfs_in = []
        self.dfs_out = []

    def dfs(self, vertex):
        self.vertex_marks[vertex] = 1
        self.dfs_in.append(vertex)
        for neigh in self.__my_graph.neighbours(vertex):
            if self.vertex_marks[neigh] == 0:
                self.dfs(neigh)

        self.vertex_marks[vertex] = 2
        self.dfs_out.append(vertex)


if __name__ == "__main__":
    import graph
    print("Example 1:")
    gp_m_1 = DFSPath(graph.adj_m_1)
    gp_m_1.dfs(0)
    print("DFS IN MATRIX: {}".format(gp_m_1.dfs_in))
    print("DFS OUT MATRIX: {}".format(gp_m_1.dfs_out))
    gp_s_1 = DFSPath(graph.adj_s_1)
    gp_s_1.dfs(0)
    print("DFS IN SET: {}".format(gp_s_1.dfs_in))
    print("DFS OUT SET: {}".format(gp_s_1.dfs_out))
    print("Example 2:")
    gp_m_2 = DFSPath(graph.adj_m_2)
    gp_m_2.dfs(0)
    print("DFS IN MATRIX: {}".format(gp_m_2.dfs_in))
    print("DFS OUT MATRIX: {}".format(gp_m_2.dfs_out))
    gp_s_2 = DFSPath(graph.adj_s_2)
    gp_s_2.dfs(0)
    print("DFS IN SET: {}".format(gp_s_2.dfs_in))
    print("DFS OUT SET: {}".format(gp_s_2.dfs_out))
