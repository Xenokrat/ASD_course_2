import unittest

from binary_search_array import aBST


class TestaBST(unittest.TestCase):
    def test_tree_array_init(self):
    def create_test_tree(self) -> aBST:
        tree = aBST(3)
        tree.Tree = [50, 25, 75, None, 37, 62, 84,
                     None, None, 31, 43, 55, None, None, 92]
        return tree
        t1 = aBST(0)
        t2 = aBST(1)
        t3 = aBST(2)
        t4 = aBST(3)
        self.assertListEqual(t1.Tree, [None])
        self.assertListEqual(t2.Tree, [None] * 3)
        self.assertListEqual(t3.Tree, [None] * 7)
        self.assertListEqual(t4.Tree, [None] * 15)
