"""Simple matrix-based graph"""
from typing import List, Optional


class Vertex:
    """represents graph's vertex"""

    def __init__(self, val: int) -> None:
        self.Value = val

    def __repr__(self) -> str:
        return f'Vertex #{self.Value}'


class SimpleGraph:
    """represents simple matrix-based graph"""

    def __init__(self, size: int) -> None:
        self.max_vertex = size
        self.m_adjacency: List[List[int]] = [[0] * size for _ in range(size)]
        self.vertex: List[Optional[Vertex]] = [None] * size

    def AddVertex(self, value: int) -> None:
        """add new vertex with 'value' in vacant place in self.vertex
        """

        # find vacant place
        for place_index, place_val in enumerate(self.vertex):
            if place_val is None:
                self.vertex[place_index] = Vertex(value)
                return

    # v - vertex's index in self.vertex
    def RemoveVertex(self, v: int) -> None:
        """remove vertex and all it's edges"""

        # delete from self.vertex
        self.vertex[v] = None

        # delete from self.m_adjacency
        for row_val in range(self.max_vertex):
            self.m_adjacency[row_val][v] = 0

        for col_val in range(self.max_vertex):
            self.m_adjacency[v][col_val] = 0

    def IsEdge(self, v1: int, v2: int) -> bool:
        """return True if there is edge between 2 vertexes"""

        return (
            self.m_adjacency[v1][v2]
            == self.m_adjacency[v2][v1]
            == 1
        )

    def AddEdge(self, v1: int, v2: int) -> None:
        """add new edge between 2 vertexes"""

        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1: int, v2: int) -> None:
        """remove edge between 2 vertexes"""

        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
