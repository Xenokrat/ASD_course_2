"""Tests for Simple Graph class"""

import unittest

from simple_graph import SimpleGraph, Vertex


def create_test_graph() -> SimpleGraph:
    """create test graph for further testing"""

    sgraph = SimpleGraph(7)
    sgraph.m_adjacency = [
        [0, 1, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 1, 0, 0],
        [1, 0, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    sgraph.vertex = [
        Vertex(1), Vertex(2), Vertex(3), Vertex(4), Vertex(5),
        None, None
    ]

    return sgraph


class MyTestCase(unittest.TestCase):
    """testing SimpleGraph class"""

    def test_add_vertex(self):
        """test for adding new vertex"""

        sgraph = create_test_graph()
        self.assertIsNone(sgraph.vertex[5])
        sgraph.AddVertex(6)
        # there is new Vertex in list
        self.assertTrue(isinstance(sgraph.vertex[5], Vertex))
        self.assertEqual(sgraph.vertex[5].Value, 6)

        # there is no edges between new vertex and other
        for row_val in range(sgraph.max_vertex):
            self.assertEqual(sgraph.m_adjacency[row_val][6], 0)

        for col_val in range(sgraph.max_vertex):
            self.assertEqual(sgraph.m_adjacency[6][col_val], 0)

    def test_remove_vertex(self):
        """test for remove existing vertex"""

        sgraph = create_test_graph()

        # vertex with index 3 exists
        self.assertTrue(isinstance(sgraph.vertex[3], Vertex))
        self.assertEqual(sgraph.vertex[3].Value, 4)
        # there is some connections for other vertexes
        self.assertListEqual(sgraph.m_adjacency[3], [1] * 5 + [0] * 2)
        column_d = [i[3] for i in sgraph.m_adjacency]
        self.assertListEqual(column_d, [1] * 5 + [0] * 2)

        sgraph.RemoveVertex(3)

        # no vertex at index 3
        self.assertIsNone(sgraph.vertex[3])
        # no connections with other vertexes
        self.assertListEqual(sgraph.m_adjacency[3], [0] * 7)
        column_d = [i[3] for i in sgraph.m_adjacency]
        self.assertListEqual(column_d, [0] * 7)

    def test_is_edge(self):
        """test for checking if there is connection between 2 vertexes"""

        sgraph = create_test_graph()
        self.assertTrue(sgraph.IsEdge(0, 1))
        self.assertTrue(sgraph.IsEdge(1, 0))

        self.assertTrue(sgraph.IsEdge(1, 4))
        self.assertTrue(sgraph.IsEdge(4, 1))

        self.assertFalse(sgraph.IsEdge(0, 4))
        self.assertFalse(sgraph.IsEdge(4, 0))

        self.assertFalse(sgraph.IsEdge(1, 2))
        self.assertFalse(sgraph.IsEdge(2, 1))

    def test_add_edge(self):
        """test for adding new edges between 2 vertexes"""

        sgraph = create_test_graph()
        self.assertFalse(sgraph.IsEdge(0, 4))
        self.assertFalse(sgraph.IsEdge(4, 0))
        self.assertFalse(sgraph.IsEdge(1, 2))
        self.assertFalse(sgraph.IsEdge(2, 1))
        sgraph.AddEdge(0, 4)
        sgraph.AddEdge(1, 2)
        self.assertTrue(sgraph.IsEdge(0, 4))
        self.assertTrue(sgraph.IsEdge(4, 0))
        self.assertTrue(sgraph.IsEdge(1, 2))
        self.assertTrue(sgraph.IsEdge(2, 1))

    def test_remove_edge(self):
        """test for adding new vertex"""

        sgraph = create_test_graph()
        self.assertTrue(sgraph.IsEdge(0, 1))
        self.assertTrue(sgraph.IsEdge(1, 0))
        self.assertTrue(sgraph.IsEdge(1, 4))
        self.assertTrue(sgraph.IsEdge(4, 1))
        sgraph.RemoveEdge(0, 1)
        sgraph.RemoveEdge(1, 4)
        self.assertFalse(sgraph.IsEdge(0, 1))
        self.assertFalse(sgraph.IsEdge(1, 0))
        self.assertFalse(sgraph.IsEdge(1, 4))
        self.assertFalse(sgraph.IsEdge(4, 1))

    def test_depth_first_search(self):
        """testing find path between 2 vertexes"""

        sgraph = create_test_graph()
        self.assertListEqual(
            sgraph.DepthFirstSearch(0, 4),
            [sgraph.vertex[0], sgraph.vertex[1], sgraph.vertex[4]]
        )
        sgraph.RemoveEdge(0, 1)
        sgraph.RemoveEdge(0, 3)
        self.assertListEqual(
            sgraph.DepthFirstSearch(0, 4),
            [sgraph.vertex[0], sgraph.vertex[2],
             sgraph.vertex[3], sgraph.vertex[4]]
        )

    def test_depth_first_search2(self):
        """more testing find path between 2 vertexes"""

        sgraph = create_test_graph()
        sgraph.RemoveEdge(1, 3)
        sgraph.AddVertex(6)
        sgraph.AddVertex(7)
        sgraph.AddEdge(4, 5)
        sgraph.AddEdge(4, 6)
        self.assertListEqual(
            sgraph.DepthFirstSearch(0, 6),
            [sgraph.vertex[0], sgraph.vertex[1],
             sgraph.vertex[4], sgraph.vertex[6]]
        )

    def test_depth_first_search_no_path(self):
        """testing path should not exist"""

        sgraph = create_test_graph()
        sgraph.RemoveEdge(1, 4)
        sgraph.RemoveEdge(3, 4)
        self.assertListEqual(sgraph.DepthFirstSearch(0, 4), [])


if __name__ == '__main__':
    unittest.main()
