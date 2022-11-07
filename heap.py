"""Heap"""

from typing import List


class Heap:
    """Represents heap"""

    def __init__(self) -> None:
        self.HeapArray: List[int] = []  # stores non-negative nums as keys

