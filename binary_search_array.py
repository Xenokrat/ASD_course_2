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

    def AddKey(self, key: int) -> int:
        """adding key to array"""

        index: Optional[int] = self.FindKeyIndex(key)

        # return index of added or existing key, or -1 if cannot add
        if index is None:
            return -1

        if index < 0:
            self.Tree[-index] = key
            return -index

        # if index == 0, this could mean that tree is empty,
        # or we found key in 1st node in 1-node tree
        if (index == 0) and (self.Tree[0] is None):
            self.Tree[0] = key

        return index
