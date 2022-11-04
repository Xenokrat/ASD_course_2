import unittest

from binary_search_array import aBST


class TestaBST(unittest.TestCase):
    def test_tree_array_init(self):
        t1 = aBST(0)
        t2 = aBST(1)
        t3 = aBST(2)
        t4 = aBST(3)
        self.assertListEqual(t1.Tree, [None])
        self.assertListEqual(t2.Tree, [None] * 3)
        self.assertListEqual(t3.Tree, [None] * 7)
        self.assertListEqual(t4.Tree, [None] * 15)
