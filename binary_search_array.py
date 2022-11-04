from typing import List, Optional, Union


class aBST:
    """Binary search tree implemented as a array"""

    def __init__(self, depth: int) -> None:
        """calculate array size for tree with given depth"""

        def _get_recr_tree_size(depth) -> int:
            if depth < 0:
                return 0
            return pow(2, depth) + _get_recr_tree_size(depth - 1)

        tree_size = _get_recr_tree_size(depth)
        self.Tree: List[Union[int, None]] = [None] * tree_size  # array of keys

    def FindKeyIndex(self, key: int) -> Optional[int]:
        """searching key index withing array"""

        def _find_key_index(index, key):
            if index >= len(self.Tree):
                return None

            root = self.Tree[index]
            if root is None:
                return index * -1
            if root == key:
                return index
            if key < root:
                return _find_key_index(2 * index + 1, key)
            if key > root:
                return _find_key_index(2 * index + 2, key)

        return _find_key_index(0, key)  # None if not found
