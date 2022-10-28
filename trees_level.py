from trees import SimpleTree, SimpleTreeNode


class LevelTreeNode(SimpleTreeNode):
    def __init__(self, val, parent) -> None:
        super().__init__(val, parent)
        # set -1 for nodes that are not associated with any tree
        self.level = -1


class LevelTree(SimpleTree):
    def __init__(self, root: LevelTreeNode) -> None:
        super().__init__(root)
        if self.Root is not None:
            self.Root.level = 0

    def set_nodes_level(self) -> None:

        def _set_nodes_level(node: LevelTreeNode, level: int) -> None:
            node.level = level
            for i in node.Children:
                _set_nodes_level(i, level + 1)

        _set_nodes_level(self.Root, 0)

    def AddChild(self, ParentNode: LevelTreeNode,
                 NewChild: LevelTreeNode) -> None:
        super().AddChild(ParentNode, NewChild)
        NewChild.level = ParentNode.level + 1
