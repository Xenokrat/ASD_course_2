from typing import List, Optional


class SimpleTreeNode:
    def __init__(self, val, parent) -> None:
        self.NodeValue = val
        self.Parent = parent
        self.Children = []

    def __repr__(self) -> str:
        return f'Node {str(self.NodeValue)}'

    def __lt__(self, other) -> bool:
        return self.NodeValue < other.NodeValue


class SimpleTree:
    def __init__(self, root: Optional[SimpleTreeNode]) -> None:
        self.Root = root

    def AddChild(self, ParentNode: SimpleTreeNode,
                 NewChild: SimpleTreeNode) -> None:
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete: SimpleTreeNode) -> None:
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def GetAllNodes(self) -> List[SimpleTreeNode]:
        if self.Root is None:
            return []

        def _get_all_nodes(node: SimpleTreeNode) -> List[SimpleTreeNode]:
            nodes_list = [node]
            for i in node.Children:
                nodes_list.extend(_get_all_nodes(i))
            return nodes_list
        return _get_all_nodes(self.Root)

    def FindNodesByValue(self, val) -> List[SimpleTreeNode]:
        all_nodes = self.GetAllNodes()
        return [
            node for node in all_nodes
            if node.NodeValue == val
        ]
   
    def MoveNode(self, OriginalNode: SimpleTreeNode,
                 NewParent: SimpleTreeNode) -> None:
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self) -> int:
        if self.Root is None:
            return 0
        
        def _count_all_nodes(node: SimpleTreeNode) -> int:
            nodes_count = 1
            for i in node.Children:
                nodes_count += _count_all_nodes(i)
            return nodes_count
        return _count_all_nodes(self.Root)

    def LeafCount(self) -> int:
        if self.Root is None:
            return 0

        def _count_all_leafs(node: SimpleTreeNode) -> int:
            leaf_count = 0 if node.Children else 1
            for i in node.Children:
                leaf_count += _count_all_leafs(i)
            return leaf_count
        return _count_all_leafs(self.Root)
