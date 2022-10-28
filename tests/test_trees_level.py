import unittest
from trees_level import LevelTree, LevelTreeNode


class TestTrees(unittest.TestCase):
    @staticmethod
    def create_test_tree_level():
        r"""
            9
           / \
          4   17
         / \   \
        3   6   22
           / \   \
          5   7   20
        """

        root_node = LevelTreeNode(9, None)
        tree = LevelTree(root_node)

        node_4 = LevelTreeNode(4, root_node)
        root_node.Children.append(node_4)

        node_3 = LevelTreeNode(3, node_4)
        node_4.Children.append(node_3)

        node_6 = LevelTreeNode(6, node_4)
        node_4.Children.append(node_6)

        node_5 = LevelTreeNode(5, node_6)
        node_6.Children.append(node_5)

        node_7 = LevelTreeNode(7, node_6)
        node_6.Children.append(node_7)

        node_17 = LevelTreeNode(17, root_node)
        root_node.Children.append(node_17)

        node_22 = LevelTreeNode(22, node_17)
        node_17.Children.append(node_22)

        node_20 = LevelTreeNode(20, node_22)
        node_22.Children.append(node_20)

        nodes = {
            'root': root_node,
            'node_4': node_4,
            'node_3': node_3,
            'node_6': node_6,
            'node_5': node_5,
            'node_7': node_7,
            'node_17': node_17,
            'node_22': node_22,
            'node_20': node_20,
        }

        return tree, nodes

    def test_set_nodes_level(self) -> None:
        tree, nodes = self.create_test_tree_level()
        tree.set_nodes_level()
        self.assertEqual(nodes['root'].level, 0)
        self.assertEqual(nodes['node_4'].level, 1)
        self.assertEqual(nodes['node_17'].level, 1)
        self.assertEqual(nodes['node_3'].level, 2)
        self.assertEqual(nodes['node_6'].level, 2)
        self.assertEqual(nodes['node_22'].level, 2)
        self.assertEqual(nodes['node_5'].level, 3)
        self.assertEqual(nodes['node_7'].level, 3)
        self.assertEqual(nodes['node_20'].level, 3)

    def test_add_child(self) -> None:
        tree, nodes = self.create_test_tree_level()
        tree.set_nodes_level()
        node_31 = LevelTreeNode(31, None)
        node_55 = LevelTreeNode(55, None)
        tree.AddChild(nodes['root'], node_31)
        tree.AddChild(nodes['node_20'], node_55)
        self.assertEqual(node_31.level, 1)
        self.assertEqual(node_55.level, 4)



if __name__ == '__main__':
    unittest.main()
