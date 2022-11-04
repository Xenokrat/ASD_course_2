from typing import Optional


class aBST:
    """Binary search tree implemented as a array"""

    def __init__(self, depth: int) -> None:
        # calculate array size for tree with given depth
        # recr version

        def _get_recr_tree_size(depth):
            if depth < 0:
                return 0
            return pow(2, depth) + _get_recr_tree_size(depth - 1)

        tree_size = _get_recr_tree_size(depth)
        self.Tree = [None] * tree_size  # array of keys
