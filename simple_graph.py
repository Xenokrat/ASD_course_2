"""Simple matrix-based graph"""
from typing import List, Optional, Any


class Queue:
    """represents queue"""

    def __init__(self) -> None:
        self.array = []

    def enqueue(self, item: Any):
        """add item to queue"""

        self.array.insert(0, item)

    def dequeue(self):
        """get item and delete from queue"""

        if not self.array:
            return None
        return self.array.pop()

    def size(self):
        """returns size of queue"""

        return len(self.array)


class Vertex:
    """represents graph's vertex"""

    def __init__(self, val: int) -> None:
        self.Value = val
        self.Hit = False
        self.bfs_previous: Optional[int] = None

    def __repr__(self) -> str:
        return f'Vertex #{self.Value}'


class SimpleGraph:
    """represents simple matrix-based graph"""

    def __init__(self, size: int) -> None:
        self.max_vertex = size
        self.m_adjacency: List[List[int]] = [[0] * size for _ in range(size)]
        self.vertex: List[Optional[Vertex]] = [None] * size
        self._bfs_queue: Queue = Queue()

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
        self._reset_vertexes()
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

    def BreadthFirstSearch(self, VFrom: int, VTo: int) -> List[Vertex]:
        """
        Find path between VFrom and VTo
        Finds optimal path, searching wide
        Params:
            VFrom (int): index of starting Vertex
            VTo (int): index of ending Vertex

        Return:
            List of Vertexes between Vertex[VFrom] and Vertex[VTo]
        """

        self._reset_vertexes()
        self._bfs_queue.array = []
        self.vertex[VFrom].Hit = True

        if not self._breadth_first_search(VFrom, VTo):
            return []

        path_vertexes = [self.vertex[VTo]]
        prev_index = self.vertex[VTo].bfs_previous
        while True:
            path_vertexes.insert(0, self.vertex[prev_index])
            prev_index = self.vertex[prev_index].bfs_previous
            if prev_index is None:
                break
        return path_vertexes

    def _breadth_first_search(
            self,
            current_index: int,
            end_index: int
    ) -> bool:
        """will return True is path is found"""

        for vert_index, edge in enumerate(self.m_adjacency[current_index]):

            # check is vertex is found
            if (vert_index == end_index) and (edge == 1):
                self.vertex[end_index].bfs_previous = current_index
                return True

            # check if we should add unchecked vertex to queue
            if (
                (self.vertex[vert_index] is not None)
                and (edge == 1)
                and (self.vertex[vert_index].Hit is False)
            ):
                self.vertex[vert_index].Hit = True
                self._bfs_queue.enqueue(vert_index)
                self.vertex[vert_index].bfs_previous = current_index

        if self._bfs_queue.size() == 0:
            return False

        current_index = self._bfs_queue.dequeue()
        return self._breadth_first_search(current_index, end_index)

    def _reset_vertexes(self) -> None:
        """clean vertexes status to preform search"""

        for vert in self.vertex:
            if vert is not None:
                vert.Hit = False
                vert.bfs_previous = None

    def WeakVertices(self) -> List[Vertex]:
        """
        Find all vertices that are not part of any triangles

        Return:
            List of "weak" vertices
        """

        weak_vert_list: List[Vertex] = []
        for vertex_index, vertex in enumerate(self.vertex):
            if vertex is None:
                continue

            # get list of adjacent vertices
            adj_vertices_ind = [
                vert_ind
                for vert_ind, edge in enumerate(self.m_adjacency[vertex_index])
                if edge == 1
            ]

            if len(adj_vertices_ind) < 2:
                weak_vert_list.append(vertex)
                continue

            # check if any of them are connected
            adj_vert_count = len(adj_vertices_ind)
            is_part_of_triangle  = any([
                self.IsEdge(adj_vertices_ind[x], adj_vertices_ind[y])
                for x in range(adj_vert_count - 1)
                for y in range(x + 1, adj_vert_count)
            ])

            if not is_part_of_triangle:
                weak_vert_list.append(vertex)

        return weak_vert_list

