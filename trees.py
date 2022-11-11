"""Simple tree with class SimpleTree and nodes SimpleTreeNode"""

from typing import List, Optional


class SimpleTreeNode:
    """represents tree node"""

    def __init__(self, val, parent) -> None:
        self.NodeValue = val
        self.Parent = parent
        self.Children = []

    def __repr__(self) -> str:
        return f"Node {str(self.NodeValue)}"

    def __lt__(self, other) -> bool:
        return self.NodeValue < other.NodeValue


class SimpleTree:
    """represents simple tree"""

    def __init__(self, root: Optional[SimpleTreeNode]) -> None:
        self.Root = root

    def AddChild(
        self,
        ParentNode: SimpleTreeNode,
        NewChild: SimpleTreeNode
    ) -> None:
        """add child to selected parent node"""

        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete: SimpleTreeNode) -> None:
        """delete selected node"""

        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def GetAllNodes(self) -> List[SimpleTreeNode]:
        """recursively return list of all nodes in tree"""

        if self.Root is None:
            return []

        return self._get_all_nodes(self.Root)

    def FindNodesByValue(self, val) -> List[SimpleTreeNode]:
        """find all nodes with given value"""

        all_nodes = self.GetAllNodes()
        return [node for node in all_nodes if node.NodeValue == val]

    def MoveNode(
        self,
        OriginalNode: SimpleTreeNode,
        NewParent: SimpleTreeNode
    ) -> None:
        """Move node with subtree to other node"""

        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self) -> int:
        """return count of all nodes in the tree"""

        if self.Root is None:
            return 0

        return self._count_all_nodes(self.Root)

    def LeafCount(self) -> int:
        """returns count of all leafs withing the tree"""

        if self.Root is None:
            return 0

        return self._count_all_leafs(self.Root)

    def EvenTrees(self) -> List[SimpleTreeNode]:
        """
        Find forest consists of even-nodes trees, after deleting maximum
        amount of edges between adjacent nodes

        Returns:
            list of paired adjacent nodes to delete edges between
        """

        edges_to_remove = []
        if self.Root is None:
            return edges_to_remove

        # if tree consists of odd number of nodes,
        # it's impossible to make even trees forest
        if self._count_all_nodes(self.Root) % 2 == 1:
            return edges_to_remove

        return self._even_trees(self.Root, edges_to_remove)

    def _even_trees(
        self,
        root: SimpleTreeNode,
        edges_to_remove: List[SimpleTreeNode]
    ) -> List[SimpleTreeNode]:
        """recursive call for self.EvenTrees"""

        for child in root.Children:
            subtree_size = self._count_all_nodes(child)
            if subtree_size % 2 == 0:
                edges_to_remove.extend([root, child])
            self._even_trees(child, edges_to_remove)

        return edges_to_remove

    def _count_all_nodes(self, node: SimpleTreeNode) -> int:
        """returns count of nodes from given node"""

        nodes_count = 1
        for i in node.Children:
            nodes_count += self._count_all_nodes(i)
        return nodes_count

    def _get_all_nodes(self, node: SimpleTreeNode) -> List[SimpleTreeNode]:
        """recursive call for self.GetAllNodes method"""

        nodes_list = [node]
        for i in node.Children:
            nodes_list.extend(self._get_all_nodes(i))
        return nodes_list

    def _count_all_leafs(self, node: SimpleTreeNode) -> int:
        """recursive call for self.LeafCount method"""

        leaf_count = 0 if node.Children else 1
        for i in node.Children:
            leaf_count += self._count_all_leafs(i)
        return leaf_count
