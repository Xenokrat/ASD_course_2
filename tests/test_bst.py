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
    def create_test_tree(self) -> BST:
        node_8  = BSTNode(8,  '', None)
        node_4  = BSTNode(4,  '', node_8)
        node_12 = BSTNode(12, '', None)
        node_8.LeftChild  = node_4
        node_8.RightChild = node_12
        node_2  = BSTNode(2,  '', None)
        node_6  = BSTNode(6,  '', None)
        node_4.LeftChild  = node_2
        node_4.RightChild = node_6
        node_10 = BSTNode(10, '', None)
        node_14 = BSTNode(14, '', None)
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

    def test_find_node_by_key(self) -> None:
        pass

    def test_add_key_value(self) -> None:
        pass

    def test_create_fin_min_max(self) -> None:
        pass

    def test_delete_node_by_key(self) -> None:
        pass

    def test_count(self) -> None:
        btree, _ = self.create_test_tree()
        self.assertEqual(btree.Count(), 7)



if __name__ == '__main__':
    unittest.main()
