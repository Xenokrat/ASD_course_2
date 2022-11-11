"""Tests for class SimpleTree"""

import unittest

from trees import SimpleTree, SimpleTreeNode


def create_test_tree():
    r"""
        9
       / \
      4   17
     / \   \
    3   6   22
       / \   \
      5   7   20
    """

    root_node = SimpleTreeNode(9, None)
    tree = SimpleTree(root_node)

    node_4 = SimpleTreeNode(4, None)
    tree.AddChild(tree.Root, node_4)

    node_3 = SimpleTreeNode(3, None)
    tree.AddChild(node_4, node_3)

    node_6 = SimpleTreeNode(6, None)
    tree.AddChild(node_4, node_6)

    node_5 = SimpleTreeNode(5, None)
    tree.AddChild(node_6, node_5)

    node_7 = SimpleTreeNode(7, None)
    tree.AddChild(node_6, node_7)

    node_17 = SimpleTreeNode(17, None)
    tree.AddChild(tree.Root, node_17)

    node_22 = SimpleTreeNode(22, None)
    tree.AddChild(node_17, node_22)

    node_20 = SimpleTreeNode(20, None)
    tree.AddChild(node_22, node_20)

    return tree, [root_node, node_4, node_3, node_6, node_5,
                  node_7, node_17, node_22, node_20]


class TestTrees(unittest.TestCase):

    def test_add_child(self) -> None:
        root_node = SimpleTreeNode(9, None)
        tree = SimpleTree(root_node)
        
        node_4 = SimpleTreeNode(4, None)
        tree.AddChild(tree.Root, node_4)

        node_3 = SimpleTreeNode(3, None)
        tree.AddChild(node_4, node_3)
        
        node_17 = SimpleTreeNode(17, None)
        tree.AddChild(tree.Root, node_17)

        self.assertIn(node_4, tree.Root.Children)
        self.assertEqual(node_4.Parent, tree.Root)

        self.assertIn(node_17, tree.Root.Children)
        self.assertEqual(node_17.Parent, tree.Root)

        self.assertIn(node_3, node_4.Children)
        self.assertEqual(node_3.Parent, node_4)

    def test_delete_node(self) -> None:
        tree, nodes = create_test_tree()
        tree.DeleteNode(nodes[1])
        self.assertEqual(tree.GetAllNodes(), [nodes[0]] + nodes[6:])
        
    def test_get_all_nodes(self) -> None:
        tree, nodes = create_test_tree()
        nodes.sort()
        nodes_list = sorted(tree.GetAllNodes())
        self.assertListEqual(nodes_list, nodes)

    def test_find_nodes_by_value(self) -> None:
        tree, nodes = create_test_tree()
        node_17_2 = SimpleTreeNode(17, nodes[8])
        tree.AddChild(nodes[8], node_17_2)
        self.assertListEqual(tree.FindNodesByValue(17), [nodes[6], node_17_2])

    def test_move_node(self) -> None:
        r"""
            9               9
           / \             / \
          4   17          4   17
         / \   \    ->   /   / \
        3   6   22      3   6   22
           / \   \         / \   \
          5   7   20      5   7   20
        """
        tree, nodes = create_test_tree()
        tree.MoveNode(nodes[3], nodes[6])
        self.assertNotIn(nodes[3], nodes[1].Children)
        self.assertIn(nodes[3], nodes[6].Children)
        self.assertIs(nodes[3].Parent, nodes[6])


    def test_count(self) -> None:
        tree, _ = create_test_tree()
        self.assertEqual(tree.Count(), 9)

        empty_tree = SimpleTree(None)
        self.assertEqual(empty_tree.Count(), 0)

    def test_leaf_count(self) -> None:
        tree, _ = create_test_tree()
        self.assertEqual(tree.LeafCount(), 4)

        empty_tree = SimpleTree(None)
        self.assertEqual(empty_tree.LeafCount(), 0)

    def test_even_tree(self) -> None:
        node_1 = SimpleTreeNode(1, None)
        tree = SimpleTree(node_1)
        node_2 = SimpleTreeNode(2, None)
        node_5 = SimpleTreeNode(5, None)
        node_7 = SimpleTreeNode(7, None)
        node_3 = SimpleTreeNode(3, None)
        node_6 = SimpleTreeNode(6, None)
        node_4 = SimpleTreeNode(6, None)
        node_8 = SimpleTreeNode(6, None)
        node_9 = SimpleTreeNode(6, None)
        node_10 = SimpleTreeNode(6, None)
        tree.AddChild(tree.Root, node_2)
        tree.AddChild(tree.Root, node_3)
        tree.AddChild(tree.Root, node_6)
        tree.AddChild(node_2, node_5)
        tree.AddChild(node_2, node_7)
        tree.AddChild(node_3, node_4)
        tree.AddChild(node_6, node_8)
        tree.AddChild(node_8, node_9)
        tree.AddChild(node_8, node_10)

        self.assertListEqual(
            tree.EvenTrees(),
            [node_1, node_3, node_1, node_6]
        )

    def test_even_tree2(self) -> None:
        tree, nodes = create_test_tree()
        self.assertListEqual(
            tree.EvenTrees(),
            []
        )


if __name__ == '__main__':
    unittest.main()
