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
        self.Node: Optional[BSTNode] = None  # None if zero nodes in tree:
        self.NodeHasKey = False
        self.ToLeft = False

    def __repr__(self) -> str:
        return f"""BSTFind(Node: {self.Node},
                   HasKey: {self.NodeHasKey},
                   ToLeft: {self.ToLeft})"""


class BST:

    def printTree(self, node: BSTNode, level=0) -> None:
        if node != None:
            self.printTree(node.RightChild, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.NodeKey))
            self.printTree(node.LeftChild, level + 1)

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
        # insert into empty tree
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

        # return False if node not found
        if (not bst_find.NodeHasKey) or (bst_find.Node is None):
            return False

        node_to_delete = bst_find.Node

        if node_to_delete.LeftChild is None:
            self._replace_node(node_to_delete, node_to_delete.RightChild)
            return

        if node_to_delete.RightChild is None:
            self._replace_node(node_to_delete, node_to_delete.LeftChild)
            return

        successor = self.FinMinMax(node_to_delete.RightChild, False)
        if successor is not None:
            self._replace_node(successor, successor.RightChild)
        self._replace_node(node_to_delete, successor)

        successor.LeftChild = node_to_delete.LeftChild
        if successor.LeftChild is not None:
            successor.LeftChild.Parent = successor

        successor.RightChild = node_to_delete.RightChild
        if successor.RightChild is not None:
            successor.RightChild.Parent = successor

    def _replace_node(self,
                      node_to_delete: Optional[BSTNode],
                      successor: Optional[BSTNode]) -> None:

        if node_to_delete is None:
            return
        elif node_to_delete.Parent is None:
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

