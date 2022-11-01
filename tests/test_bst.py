from typing import Tuple, Dict
import unittest

from binary_search_trees import *


class TestBST(unittest.TestCase):
    r"""
        8
       / \
      4   12
     / \  / \
    2  6  10 14
    """

    def printTree(self, node: BSTNode, level=0) -> None:
        if node != None:
            self.printTree(node.RightChild, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.NodeKey))
            self.printTree(node.LeftChild, level + 1)

    def create_test_tree(self) -> Tuple[BST, Dict[str, BSTNode]]:
        node_8  = BSTNode(8,  '', None)
        node_4  = BSTNode(4,  '', node_8)
        node_12 = BSTNode(12, '', node_8)
        node_2  = BSTNode(2,  '', node_4)
        node_6  = BSTNode(6,  '', node_4)
        node_10 = BSTNode(10, '', node_12)
        node_14 = BSTNode(14, '', node_12)
        node_4.LeftChild  = node_2
        node_4.RightChild = node_6
        node_8.LeftChild  = node_4
        node_8.RightChild = node_12
        node_12.LeftChild  = node_10
        node_12.RightChild = node_14

        nodes = {
            'node_8' : node_8,
            'node_4' : node_4,
            'node_12': node_12,
            'node_2' : node_2,
            'node_6' : node_6,
            'node_10': node_10,
            'node_14': node_14,
        }
        return BST(node_8), nodes

    def test_found_node_by_key(self) -> None:
        tree, nodes = self.create_test_tree()
        bst_find = tree.FindNodeByKey(10)
        self.assertIs(bst_find.Node, nodes['node_10'], 'existing node not found')
        self.assertTrue(bst_find.NodeHasKey, 'NodeHasKey not True')

    def test_not_found_node_left(self) -> None:
        tree, nodes = self.create_test_tree()
        bst_find = tree.FindNodeByKey(16)
        self.assertIs(bst_find.Node, nodes['node_14'], 'parent node not found')
        self.assertFalse(bst_find.NodeHasKey, 'NodeHasKey not False')
        self.assertFalse(bst_find.ToLeft)

    def test_not_found_node_right(self) -> None:
        tree, nodes = self.create_test_tree()
        bst_find = tree.FindNodeByKey(5)
        self.assertIs(bst_find.Node, nodes['node_6'], 'parent node not found')
        self.assertFalse(bst_find.NodeHasKey, 'NodeHasKey not False')
        self.assertTrue(bst_find.ToLeft)

    def test_find_in_empty_tree(self) -> None:
        tree = BST(None)
        bst_find = tree.FindNodeByKey(1)
        self.assertIsNone(bst_find.Node)

    def test_add_key_value_left(self) -> None:
        tree, nodes = self.create_test_tree()
        bst_find = tree.FindNodeByKey(7)
        self.assertFalse(bst_find.NodeHasKey)

        tree.AddKeyValue(7, 'kek')
        bst_find = tree.FindNodeByKey(7)
        self.assertTrue(bst_find.NodeHasKey)
        self.assertIs(nodes['node_6'].RightChild, bst_find.Node)
    
    def test_add_key_value_right(self) -> None:
        tree, nodes = self.create_test_tree()
        bst_find = tree.FindNodeByKey(1)
        self.assertFalse(bst_find.NodeHasKey)

        tree.AddKeyValue(1, 'kek')
        bst_find = tree.FindNodeByKey(1)
        self.assertTrue(bst_find.NodeHasKey)
        self.assertIs(nodes['node_2'].LeftChild, bst_find.Node)

    def test_add_key_value_to_empty_tree(self) -> None:
        tree = BST(None)
        tree.AddKeyValue(1, '')
        self.assertIsNotNone(tree.Root)

    def test_add_dublicated_key_value(self) -> None:
        tree, _ = self.create_test_tree()
        self.assertFalse(tree.AddKeyValue(12, ''))

    def test_find_max_from_root(self) -> None:
        tree, nodes = self.create_test_tree()
        self.assertEqual(
            tree.FinMinMax(tree.Root, True), nodes['node_14']
        )

    def test_find_min_from_root(self) -> None:
        tree, nodes = self.create_test_tree()
        self.assertEqual(
            tree.FinMinMax(tree.Root, False), nodes['node_2']
        )

    def test_find_max_from_node(self) -> None:
        tree, nodes = self.create_test_tree()
        from_node = nodes['node_4']
        self.assertEqual(
            tree.FinMinMax(from_node, True), nodes['node_6']
        )

    def test_find_min_from_node(self) -> None:
        tree, nodes = self.create_test_tree()
        from_node = nodes['node_12']
        self.assertEqual(
            tree.FinMinMax(from_node, False), nodes['node_10']
        )

    def test_delete_leaf(self) -> None:
        r"""
            8
           / \
          4   12
         / \   \
        2  6    14
        """
        tree, nodes = self.create_test_tree()
        key = 10
        tree.DeleteNodeByKey(key)
        bst_find = tree.FindNodeByKey(key)
        self.assertFalse(bst_find.NodeHasKey)
        self.assertIsNone(nodes['node_12'].LeftChild)

    def test_delete_node_one_child(self) -> None:
        r"""
            8
           / \
          4   14
         / \
        2  6
        """
        tree, nodes = self.create_test_tree()
        tree.DeleteNodeByKey(10)
        tree.DeleteNodeByKey(12)
        bst_find = tree.FindNodeByKey(12)
        self.assertFalse(bst_find.NodeHasKey)
        self.assertIs(nodes['node_8'].RightChild, nodes['node_14'])
        self.assertIs(nodes['node_14'].Parent, nodes['node_8'])

    def test_delete_node_two_children(self) -> None:
        r"""
            8
           / \
          4   14
         / \  / 
        2  6  10
        """
        tree, nodes = self.create_test_tree()
        tree.DeleteNodeByKey(12)
        bst_find = tree.FindNodeByKey(12)
        self.assertFalse(bst_find.NodeHasKey)
        self.assertIs(nodes['node_8'].RightChild, nodes['node_14'])
        self.assertIs(nodes['node_14'].Parent, nodes['node_8'])
        self.assertIs(nodes['node_14'].LeftChild, nodes['node_10'])
        self.assertIs(nodes['node_10'].Parent, nodes['node_14'])

    def test_delete_root_node(self) -> None:
        r"""
            10
           / \
          4   12
         / \   \
        2  6    14
        """
        tree, nodes = self.create_test_tree()
        tree.DeleteNodeByKey(8)
        bst_find = tree.FindNodeByKey(8)
        self.assertFalse(bst_find.NodeHasKey)
        self.assertIs(tree.Root, nodes['node_10'])
        self.assertIs(nodes['node_10'].RightChild, nodes['node_12'])
        self.assertIs(nodes['node_10'].LeftChild, nodes['node_4'])
        self.assertIs(nodes['node_12'].Parent, nodes['node_10'])
        self.assertIs(nodes['node_12'].RightChild, nodes['node_14'])
        self.assertIsNone(nodes['node_12'].LeftChild)

    def test_delete_last_node(self) -> None:
        r""" 8 """
        node_8 = BSTNode(8, '', None)
        tree = BST(node_8)
        bst_find = tree.FindNodeByKey(8)
        self.assertTrue(bst_find.NodeHasKey)
        tree.DeleteNodeByKey(8)
        bst_find = tree.FindNodeByKey(8)
        self.assertIsNone(bst_find.Node)
        self.assertIsNone(tree.Root)
        self.assertIsNone(node_8.Parent)

    def test_count(self) -> None:
        btree, _ = self.create_test_tree()
        self.assertEqual(btree.Count(), 7)


if __name__ == '__main__':
    unittest.main()

    def test_count(self) -> None:
        btree, _ = self.create_test_tree()
        self.assertEqual(btree.Count(), 7)


if __name__ == '__main__':
    unittest.main()
