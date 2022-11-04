import unittest

from binary_search_array import aBST


class TestaBST(unittest.TestCase):
    def create_test_tree(self) -> aBST:
        tree = aBST(3)
        tree.Tree = [50, 25, 75, None, 37, 62, 84,
                     None, None, 31, 43, 55, None, None, 92]
        return tree

    def test_tree_array_init(self) -> None:
        t1 = aBST(0)
        t2 = aBST(1)
        t3 = aBST(2)
        t4 = aBST(3)
        self.assertListEqual(t1.Tree, [None])
        self.assertListEqual(t2.Tree, [None] * 3)
        self.assertListEqual(t3.Tree, [None] * 7)
        self.assertListEqual(t4.Tree, [None] * 15)

    def test_find_existing_key(self) -> None:
        tree = self.create_test_tree()
        index = tree.FindKeyIndex(55)
        self.assertEqual(index, 11)

    def test_find_new_key_index(self) -> None:
        tree = self.create_test_tree()
        index = tree.FindKeyIndex(70)
        self.assertEqual(index, -12)

    def test_cannot_find_index(self) -> None:
        tree = self.create_test_tree()
        index = tree.FindKeyIndex(100)
        self.assertIsNone(index)

    def test_return_index_from_empty_tree(self) -> None:
        tree = aBST(0)
        index = tree.FindKeyIndex(1)
        self.assertEqual(index, 0)

        # same return from tree with one node
        tree.Tree[0] = 1
        index = tree.FindKeyIndex(1)
        self.assertEqual(index, 0)

        index = tree.FindKeyIndex(2)
        self.assertIsNone(index)

    def test_add_existing_key(self) -> None:
        tree = self.create_test_tree()
        add_key_res = tree.AddKey(37)
        self.assertEqual(add_key_res, 4)
        # check that Tree array not changed
        self.assertListEqual(tree.Tree, self.create_test_tree().Tree)

    def test_add_new_key(self) -> None:
        tree = self.create_test_tree()
        add_key_res = tree.AddKey(80)
        self.assertEqual(add_key_res, 13)
        self.assertEqual(tree.Tree[13], 80)

    def test_cannot_add_key(self) -> None:
        tree = self.create_test_tree()
        add_key_res = tree.AddKey(52)
        self.assertEqual(add_key_res, -1)
        # check that Tree array not changed
        self.assertListEqual(tree.Tree, self.create_test_tree().Tree)

    def test_add_existing_root(self) -> None:
        tree = aBST(0)
        tree.Tree[0] = 1
        add_key_res = tree.AddKey(1)
        self.assertEqual(add_key_res, 0)

    def test_add_in_empty_tree(self) -> None:
        tree = aBST(0)
        add_key_res = tree.AddKey(5)
        self.assertEqual(add_key_res, 0)
        self.assertEqual(tree.Tree[0], 5)
