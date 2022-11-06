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


class BalancedBST:
    """Binary tree representation"""

    def __init__(self) -> None:
        self.Root = None

    def GenerateTree(self, a: List[int]):
        """Create a tree from non-sorted array 'a'"""

    def IsBalanced(self, root_node: BSTNode) -> bool:
        """Check if tree part from root_node is balanced"""
        return False
