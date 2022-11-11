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

        def _get_all_nodes(node: SimpleTreeNode) -> List[SimpleTreeNode]:
            nodes_list = [node]
            for i in node.Children:
                nodes_list.extend(_get_all_nodes(i))
            return nodes_list

        return _get_all_nodes(self.Root)

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

        def _count_all_leafs(node: SimpleTreeNode) -> int:
            leaf_count = 0 if node.Children else 1
            for i in node.Children:
                leaf_count += _count_all_leafs(i)
            return leaf_count

        return _count_all_leafs(self.Root)
