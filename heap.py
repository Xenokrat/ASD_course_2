"""Heap"""

from typing import List


class Heap:
    """Represents heap"""

    def __init__(self) -> None:
        self.HeapArray: List[int] = []  # stores non-negative nums as keys

    def MakeHeap(self, a, depth) -> None:
        """create HeapArray from array 'a' with given 'depth'"""

        heap_size = pow(2, depth + 1) - 1
        if len(a) > heap_size:
            return

        self.HeapArray = [None] * heap_size
        for key in a:
            self.Add(key)

    def GetMax(self) -> int:
        """return root key and re-built heap"""

        if not self.HeapArray:
            return -1  # -1 if heap is emptY

        max_value = self.HeapArray[0]
        # 1 grab last non-none value
        index = -1
        while -index <= len(self.HeapArray):
            if self.HeapArray[index] is not None:
                key = self.HeapArray[index]
                self.HeapArray[0] = key
                self.HeapArray[index] = None
                self._shift_down(key, index)
                break
            index -= 1

        return max_value

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

