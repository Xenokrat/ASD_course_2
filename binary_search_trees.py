from __future__ import annotations
from typing import Optional, Any, Tuple, List


class BSTNode:

    def __init__(self, key: int, val: Any,
                 parent: Optional[BSTNode]) -> None:
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild: Optional[BSTNode] = None
        self.RightChild: Optional[BSTNode] = None

    def __repr__(self) -> str:
        return f"NodeKey {self.NodeKey}"


class BSTFind:

    def __init__(self) -> None:
        self.Node: Optional[BSTNode] = None  # None if zero nodes in tree:
        self.NodeHasKey = False
        self.ToLeft = False

    def __repr__(self) -> str:
        return f"""BSTFind(Node: {self.Node},
                   HasKey: {self.NodeHasKey},
                   ToLeft: {self.ToLeft})"""


class BST:

    def __init__(self, node: Optional[BSTNode]) -> None:
        self.Root = node

    def FindNodeByKey(self, key: int) -> BSTFind:
        bst_find = BSTFind()
        node = self.Root

        if node is None:
            return bst_find

        while node is not None:
            bst_find.Node = node
            if key == node.NodeKey:
                bst_find.NodeHasKey = True
                return bst_find
            if key < node.NodeKey:
                bst_find.ToLeft = True
                node = node.LeftChild
            else:
                bst_find.ToLeft = False
                node = node.RightChild
        return bst_find

    def AddKeyValue(self, key: int, val: Any) -> bool:
        bst_find = self.FindNodeByKey(key)
        if bst_find.NodeHasKey:
            return False
        # insert into empty tree
        if bst_find.Node is None:
            self.Root = BSTNode(key, val, None)
            return True

        node_to_insert = BSTNode(key, val, bst_find.Node)
        if bst_find.ToLeft:
            bst_find.Node.LeftChild = node_to_insert
        else:
            bst_find.Node.RightChild = node_to_insert
        return True

    def FinMinMax(self,
                  FromNode: Optional[BSTNode],
                  FindMax: bool) -> Optional[BSTNode]:

        node = FromNode
        if node is None:
            return None
        while True:
            next_node = (
                node.RightChild if FindMax
                else node.LeftChild
            )
            if next_node is None:
                return node
            node = next_node

    def DeleteNodeByKey(self, key: int) -> bool:
        bst_find = self.FindNodeByKey(key)

        # return False if node not found
        if (not bst_find.NodeHasKey) or (bst_find.Node is None):
            return False

        node_to_delete = bst_find.Node
        if node_to_delete.LeftChild is None:
            self._replace_node(node_to_delete, node_to_delete.RightChild)
            return True

        if node_to_delete.RightChild is None:
            self._replace_node(node_to_delete, node_to_delete.LeftChild)
            return True

        successor = self.FinMinMax(node_to_delete.RightChild, False)
        if successor is not None:
            self._replace_node(successor, successor.RightChild)
        self._replace_node(node_to_delete, successor)

        if successor is None:
            return True
        successor.LeftChild = node_to_delete.LeftChild
        if successor.LeftChild is not None:
            successor.LeftChild.Parent = successor
        successor.RightChild = node_to_delete.RightChild
        if successor.RightChild is not None:
            successor.RightChild.Parent = successor
        return True

    def _replace_node(self,
                      node_to_delete: Optional[BSTNode],
                      successor: Optional[BSTNode]) -> None:

        if node_to_delete is None:
            return
        if node_to_delete.Parent is None:
            self.Root = successor
        elif node_to_delete.Parent.LeftChild is node_to_delete:
            node_to_delete.Parent.LeftChild = successor
        elif node_to_delete.Parent.RightChild is node_to_delete:
            node_to_delete.Parent.RightChild = successor

        if successor is not None:
            successor.Parent = node_to_delete.Parent

    def Count(self) -> int:

        def _count(node: Optional[BSTNode]) -> int:
            if node is None:
                return 0
            return _count(node.LeftChild) + _count(node.RightChild) + 1
        return _count(self.Root)

    def WideAllNodes(self) -> Tuple[BSTNode]:

        # return empty tuple if tree is empty
        if self.Root is None:
            return tuple()

        result_nodes_list: List[BSTNode] = []
        current_nodes: List[BSTNode] = [self.Root]  # nodes on level n

        while True:
            if not current_nodes:
                return tuple(result_nodes_list)
            next_nodes = []  # nodes on level n + 1

            for node in current_nodes:
                if node.LeftChild is not None:
                    next_nodes.append(node.LeftChild)
                if node.RightChild is not None:
                    next_nodes.append(node.RightChild)

            result_nodes_list.extend(current_nodes)
            current_nodes = next_nodes.copy()

    def DeepAllNodes(self, search_type: int) -> Tuple[BSTNode]:

        # return from empty tree
        if self.Root is None:
            return tuple()

        if search_type == 0:
            return tuple(self._get_all_nodes_in_order(self.Root, []))

        if search_type == 1:
            return tuple(self._get_all_nodes_post_order(self.Root, []))

        if search_type == 2:
            return tuple(self._get_all_nodes_pre_order(self.Root, []))

        return tuple()

    def _get_all_nodes_in_order(
        self,
        root: Optional[BSTNode],
        result_nodes_list: List[BSTNode]
    ) -> List[BSTNode]:

        if root is not None:
            # 1 in-order
            self._get_all_nodes_in_order(root.LeftChild, result_nodes_list)
            result_nodes_list.append(root)
            self._get_all_nodes_in_order(root.RightChild, result_nodes_list)

        return result_nodes_list

    def _get_all_nodes_post_order(
        self,
        root: Optional[BSTNode],
        result_nodes_list: List[BSTNode]
    ) -> List[BSTNode]:

        if root is not None:
            # 2 post order
            self._get_all_nodes_post_order(root.LeftChild, result_nodes_list)
            self._get_all_nodes_post_order(root.RightChild, result_nodes_list)
            result_nodes_list.append(root)

        return result_nodes_list

    def _get_all_nodes_pre_order(
        self,
        root: Optional[BSTNode],
        result_nodes_list: List[BSTNode]
    ) -> List[BSTNode]:

        if root is not None:
            # 3 pre order
            result_nodes_list.append(root)
            self._get_all_nodes_pre_order(root.LeftChild, result_nodes_list)
            self._get_all_nodes_pre_order(root.RightChild, result_nodes_list)

        return result_nodes_list
