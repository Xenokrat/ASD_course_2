"""Create binary search tree from array,
   check if created tree is balanced
"""

from __future__ import annotations
from typing import List, Optional


class BSTNode:
    """Binary tree node representation"""

    def __init__(self, key: int, parent: Optional[BSTNode]) -> None:
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0

    def set_node_level(self) -> None:
        if self.Parent is not None:
            self.Level = self.Parent.Level + 1


class BalancedBST:
    """Binary tree representation"""

    def __init__(self) -> None:
        self.Root = None

    def GenerateTree(self, a: List[int]) -> None:
        """Create a tree from non-sorted array 'a'"""

        a.sort()
        self.Root = self._generate_tree(a, None)

    def _generate_tree(self,
                       array: List[int],
                       parent: Optional[BSTNode]) -> Optional[BSTNode]:

        # base case
        if not array:
            return None

        # create new BSTNode (root) with current key as a
        # mid-array value, set parent node from F() param
        mid = len(array) // 2
        key = array[mid]
        root = BSTNode(key, parent)

        # recursively call F() with [:mid] slice and
        # root as parent node, set root.LeftChild to F() result
        root.LeftChild = self._generate_tree(array[:mid], root)

        # same with RightChild
        root.RightChild = self._generate_tree(array[mid + 1:], root)

        return root

    def IsBalanced(self, root_node: BSTNode) -> bool:
        """Check if tree part from root_node is balanced"""
        return False
