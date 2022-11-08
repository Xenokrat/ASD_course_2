"""Heap"""

from typing import List, Union, Optional


class Heap:
    """Represents heap"""

    def __init__(self) -> None:
        # stores non-negative nums as keys
        self.HeapArray: List[Union[int, None]] = []

    def MakeHeap(self, a, depth) -> None:
        """create HeapArray from array 'a' with given 'depth'"""

        heap_size: int = pow(2, depth + 1) - 1
        if len(a) > heap_size:
            return

        self.HeapArray = [None] * heap_size
        for key in a:
            self.Add(key)

    def GetMax(self) -> int:
        """return root key and re-built heap"""

        if not self.HeapArray:
            return -1  # -1 if heap is empty

        max_value = self.HeapArray[0]
        # 1 grab last non-none value
        index = -1
        while -index <= len(self.HeapArray):
            if self.HeapArray[index] is not None:
                key = self.HeapArray[index]
                self.HeapArray[0] = key
                self.HeapArray[index] = None
                self._shift_down(key)
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

    def _shift_down(self, key: int) -> None:
        """push key down to right position"""

        index = 0
        while True:
            left_child_index: int = 2 * index + 1
            right_child_index: int = left_child_index + 1

            # exit case
            if right_child_index >= len(self.HeapArray):
                return None

            left_child_key: Optional[int] = self.HeapArray[left_child_index]
            if left_child_key is None:
                left_child_key = -1

            right_child_key: Optional[int] = self.HeapArray[right_child_index]
            if right_child_key is None:
                right_child_key = -1

            if left_child_key >= right_child_key:
                max_child_key = left_child_key
                max_child_index = left_child_index
            else:
                max_child_key = right_child_key
                max_child_index = right_child_index

            if key >= max_child_key:
                return None

            # swapping keys
            self.HeapArray[max_child_index] = key
            self.HeapArray[index] = max_child_key
            index = max_child_index
