"""Simple matrix-based graph"""
from typing import List, Optional


class Vertex:
    """represents graph's vertex"""

    def __init__(self, val: int) -> None:
        self.Value = val
        self.Hit = False

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

    def DepthFirstSearch(self, VFrom: int, VTo: int) -> List[Vertex]:
        """
        Find path between VFrom and VTo
        Params:
            VFrom (int): index of starting Vertex
            VTo (int): index of ending Vertex

        Return:
            List of Vertexes between Vertex[VFrom] and Vertex[VTo]
        """

        # prepare graph to search
        for i in self.vertex:
            if i is not None:
                i.Hit = False

        path: List[int] = []
        path_indexes = self._depth_first_search(VFrom, path, VTo)
        return [self.vertex[i] for i in path_indexes]

    def _depth_first_search(
            self,
            current_index: int,
            path: List[int],
            end_index: int
    ) -> List[int]:

        self.vertex[current_index].Hit = True
        if current_index not in path:
            path.append(current_index)

        adjacent_vertex = []
        for vertex_index, edge in enumerate(self.m_adjacency[current_index]):
            # base case -- found path
            if (vertex_index == end_index) and (edge == 1):
                path.append(vertex_index)
                return path

            # track adjacent not checked vertexes
            if (edge == 1) and (self.vertex[vertex_index].Hit is False):
                adjacent_vertex.append(vertex_index)

        if adjacent_vertex:
            return self._depth_first_search(
                adjacent_vertex[0], path, end_index
            )

        if (not adjacent_vertex) and (len(path) > 1):
            path.pop()
            return self._depth_first_search(
                path[-1], path, end_index
            )

        # there are no unchecked vertexes and only last element in path
        return []
