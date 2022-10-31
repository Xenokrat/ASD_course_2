from __future__ import annotations
from typing import Optional, Any


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
        self.Node: Optional[BSTNode] = None # None if zero nodes in tree:
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

    def AddKeyValue(self, key: int, val: Any) -> Optional[bool]:
        bst_find = self.FindNodeByKey(key)
        # instert into empty tree
        if bst_find.Node is None:
            self.Root = BSTNode(key, val, None)
            return

        if bst_find.NodeHasKey:
            return False

        node_to_insert = BSTNode(key, val, bst_find.Node)
        if bst_find.ToLeft:
            bst_find.Node.LeftChild = node_to_insert
        else:
            bst_find.Node.RightChild = node_to_insert

    def FinMinMax(self, FromNode: Optional[BSTNode],
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

    def DeleteNodeByKey(self, key: int) -> Optional[bool]:

        bst_find = self.FindNodeByKey(key)
        if not bst_find.NodeHasKey or bst_find.Node is None:
            return False  # if node not found

        node_to_delete = bst_find.Node
        has_left_child = node_to_delete.LeftChild is not None
        has_right_child = node_to_delete.RightChild is not None

        # node_to_delete is leaf
        if not (has_left_child or has_right_child):
            self._delete_no_children(node_to_delete)
            return 

        # node_to_delete has one child
        if has_left_child ^ has_right_child:
            self._delete_one_child(node_to_delete, has_left_child)
            return

        # node_to_delete has two children
        self._delete_two_children(node_to_delete)

    def Count(self) -> int:

        def _count(node: Optional[BSTNode]) -> int:
            if node is None:
                return 0
            return _count(node.LeftChild) + _count(node.RightChild) + 1
        return _count(self.Root)

    def _delete_no_children(self, node_to_delete: BSTNode) -> None:
            parent_node = node_to_delete.Parent
            if parent_node is None:  # delete Root
                self.Root = None
                return
            if node_to_delete is parent_node.LeftChild:
                parent_node.LeftChild = None
            else:
                parent_node.RightChild = None

    def _delete_one_child(self, node_to_delete: BSTNode,
                          has_left_child: bool) -> None:
        parent_node = node_to_delete.Parent
        child_node = (
            node_to_delete.LeftChild
            if has_left_child
            else node_to_delete.RightChild
        )
        if parent_node is None:  # delete Root with one child
            self.Root = child_node
            return
        if node_to_delete is parent_node.LeftChild:
            parent_node.LeftChild = child_node
        else:
            parent_node.RightChild = child_node
        if child_node:
            child_node.Parent = parent_node

    def _delete_two_children(self, node_to_delete: BSTNode) -> None:
        successor = self.FinMinMax(
            node_to_delete.RightChild,
            False
        )
        if successor is None:  # the tree is empty
            return 

        if successor.RightChild is None:
            self._delete_no_children(successor)
        else:
            self._delete_one_child(successor, has_left_child=False)

        parent_node = node_to_delete.Parent
        if parent_node is None:
            self.Root = successor
        else:
            if node_to_delete is parent_node.LeftChild:
                parent_node.LeftChild = successor
            else:
                parent_node.RightChild = successor
        successor.Parent = parent_node
        successor.LeftChild = node_to_delete.LeftChild
        successor.RightChild = node_to_delete.RightChild
        if successor.LeftChild:
            successor.LeftChild.Parent = successor
        if successor.RightChild:
            successor.RightChild.Parent = successor

