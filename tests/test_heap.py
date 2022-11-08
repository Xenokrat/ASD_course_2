"""Tests for Heap data structure"""

import unittest

from heap import Heap


class MyTestCase(unittest.TestCase):
    """Tests for Heap class"""

    def test_add(self):
        """testing add to existing tree"""

        heap = Heap()
        heap.HeapArray = [
            11, 9, 4, 7, 8, 3, 1, 2, 5, 6, None, None, None, None, None
        ]
        self.assertTrue(heap.Add(10))
        self.assertListEqual(
            heap.HeapArray,
            [11, 10, 4, 7, 9, 3, 1, 2, 5, 6, 8, None, None, None, None]
        )
        self.assertTrue(heap.Add(5))
        self.assertListEqual(
            heap.HeapArray,
            [11, 10, 5, 7, 9, 4, 1, 2, 5, 6, 8, 3, None, None, None]
        )

    def test_add_to_empty_heap(self):
        """add to empty tree"""

        heap = Heap()
        heap.HeapArray = [None]
        self.assertTrue(heap.Add(11))
        self.assertListEqual(heap.HeapArray, [11])

    def test_cannot_add(self):
        """cannot add if there is no place"""

        heap = Heap()
        heap.HeapArray = [None]
        self.assertTrue(heap.Add(11))
        self.assertFalse(heap.Add(10))

    def test_make_heap(self):
        """test creating heap from zero"""

        heap = Heap()
        array = [7, 11, 4, 9, 6, 3, 1, 2, 5, 8]
        heap.MakeHeap(array, 3)
        self.assertListEqual(
            heap.HeapArray,
            [11, 9, 4, 7, 8, 3, 1, 2, 5, 6, None, None, None, None, None]
        )

    def test_cannot_make_heap(self):
        """cannot insert array if it's too big"""

        heap = Heap()
        array = list(range(16))
        heap.MakeHeap(array, 3)
        self.assertFalse(heap.HeapArray)

    def test_get_max(self):
        pass



if __name__ == '__main__':
    unittest.main()
