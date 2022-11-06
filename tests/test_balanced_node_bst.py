"""Tests for BalancedBST class"""

import unittest
from random import shuffle

from balanced_node_bst import BalancedBST, BSTNode


def create_test_tree() -> BalancedBST:
    """Create testing tree"""

    array = list(range(1, 8))
    shuffle(array)
    tree = BalancedBST()
    tree.GenerateTree(array)
    return tree


class TestBalancedBST(unittest.TestCase):
    """BalancedBST tests"""

    def test_created_balanced_tree(self) -> None:
        """GenerateTree test, parent / child relations
           nodes level
        """

        tree = create_test_tree()
        # check root 4
        self.assertIsNotNone(tree.Root)
        self.assertEqual(tree.Root.NodeKey, 4)
        self.assertIsNone(tree.Root.Parent)
        self.assertEqual(tree.Root.Level, 0)
        # check 2
        self.assertEqual(tree.Root.LeftChild.NodeKey, 2)
        self.assertEqual(tree.Root.LeftChild.Parent.NodeKey, 4)
        self.assertEqual(tree.Root.LeftChild.Level, 1)
        # check 6
        self.assertEqual(tree.Root.RightChild.NodeKey, 6)
        self.assertEqual(tree.Root.RightChild.Parent.NodeKey, 4)
        self.assertEqual(tree.Root.RightChild.Level, 1)
        # check 1
        self.assertEqual(tree.Root.LeftChild.LeftChild.NodeKey, 1)
        self.assertEqual(tree.Root.LeftChild.LeftChild.Parent.NodeKey, 2)
        self.assertEqual(tree.Root.LeftChild.LeftChild.Level, 2)
        # check 3
        self.assertEqual(tree.Root.LeftChild.RightChild.NodeKey, 3)
        self.assertEqual(tree.Root.LeftChild.RightChild.Parent.NodeKey, 2)
        self.assertEqual(tree.Root.LeftChild.RightChild.Level, 2)
        # check 5
        self.assertEqual(tree.Root.RightChild.LeftChild.NodeKey, 5)
        self.assertEqual(tree.Root.RightChild.LeftChild.Parent.NodeKey, 6)
        self.assertEqual(tree.Root.RightChild.LeftChild.Level, 2)
        # check 7
        self.assertEqual(tree.Root.RightChild.RightChild.NodeKey, 7)
        self.assertEqual(tree.Root.RightChild.RightChild.Parent.NodeKey, 6)
        self.assertEqual(tree.Root.RightChild.RightChild.Level, 2)

    def test_is_balanced_true(self) -> None:
        """This tree should be balanced"""

        tree = create_test_tree()
        self.assertTrue(tree.IsBalanced(tree.Root))
        node_8 = BSTNode(8, tree.Root.RightChild.RightChild)
        tree.Root.RightChild.RightChild.RightChild = node_8
        # still should be balanced
        self.assertTrue(tree.IsBalanced(tree.Root))

    def test_is_balanced_false(self) -> None:
        """This tree should not be balanced"""

        tree = create_test_tree()
        node_8 = BSTNode(8, tree.Root.RightChild.RightChild)
        tree.Root.RightChild.RightChild.RightChild = node_8
        node_9 = BSTNode(9, node_8)
        node_8.RightChild = node_9
        self.assertFalse(tree.IsBalanced(tree.Root))


if __name__ == '__main__':
    unittest.main()
