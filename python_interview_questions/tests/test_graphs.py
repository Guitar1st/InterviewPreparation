from python_interview_questions.src.graphs import common as graphs_common


class TestCommon:
    weighted_edges1 = [
        # from, to, weight
        (0, 1, 1),
        (1, 2, 1),
        (2, 3, 1),
        (3, 0, 1),
    ]

    def test__adjacency_matrix_instance(self):
        directed1 = graphs_common.AdjacencyMatrix(4, self.weighted_edges1, True)
        for i in range(4):
            assert list(directed1.neighbours(i)) == [graphs_common.WeightedConnection((i + 1) % 4)]

        not_directed1 = graphs_common.AdjacencyMatrix(4, self.weighted_edges1, False)
        for i in range(4):
            assert set(not_directed1.neighbours(i)) == {
                graphs_common.WeightedConnection((i + 1) % 4),
                graphs_common.WeightedConnection((i - 1) % 4),
            }

    def test__adjacency_set_instance(self):
        directed1 = graphs_common.AdjacencySet(range(4), self.weighted_edges1, True)
        for i in range(4):
            assert list(directed1.neighbours(i)) == [graphs_common.WeightedConnection((i + 1) % 4)]
            for neighbour in directed1.neighbours(i):
                assert directed1.min_weight(i, neighbour.value) == 1

        not_directed1 = graphs_common.AdjacencySet(range(4), self.weighted_edges1, False)
        for i in range(4):
            assert set(not_directed1.neighbours(i)) == {
                graphs_common.WeightedConnection((i + 1) % 4),
                graphs_common.WeightedConnection((i - 1) % 4),
            }
            for neighbour in directed1.neighbours(i):
                assert directed1.min_weight(i, neighbour.value) == 1
        not_directed1.remove_edge(3, 0)
        assert list(not_directed1.neighbours(0)) == [graphs_common.WeightedConnection(1)]
        assert list(not_directed1.neighbours(3)) == [graphs_common.WeightedConnection(2)]
        not_directed1.remove_vertex(3)
        not_directed1.remove_vertex(2)
        assert list(not_directed1.neighbours(0)) == [graphs_common.WeightedConnection(1)]
        assert list(not_directed1.neighbours(1)) == [graphs_common.WeightedConnection(0)]

        multi_edged_graph = graphs_common.AdjacencySet(
            range(2),
            [
                (0, 1, 2),
                (0, 1, 10),
                (1, 2, 100),
            ],
            True
        )
        assert set(multi_edged_graph.neighbours(0)) == {
            graphs_common.WeightedConnection(1, 2),
            graphs_common.WeightedConnection(1, 10),
        }
        assert set(multi_edged_graph.neighbours(1)) == {
            graphs_common.WeightedConnection(2, 100),
        }
        assert multi_edged_graph.min_weight(0, 1) == 2
