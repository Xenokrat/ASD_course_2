"""Heap"""

from typing import List


class Heap:
    """Represents heap"""

    def __init__(self) -> None:
        self.HeapArray: List[int] = []  # stores non-negative nums as keys

    def Add(self, key) -> bool:
        """add new key and re-built heap"""

        if not self.HeapArray:
            return False

        # add at first non-none position
        index = 0
        while index < len(self.HeapArray):
            if self.HeapArray[index] is None:
                self.HeapArray[index] = key
                self._shift_up(key, index)
                return True
            index += 1
        return False  # if the heap is full

    def _shift_up(self, key: int, index: int) -> None:
        """push key up to right position"""

        while True:
            parent_index: int = (index - 1) // 2
            if parent_index < 0:
                return None

            parent_key: int = self.HeapArray[parent_index]
            if key <= parent_key:
                return None

            # swapping keys
            self.HeapArray[parent_index] = key
            self.HeapArray[index] = parent_key
            index = parent_index

