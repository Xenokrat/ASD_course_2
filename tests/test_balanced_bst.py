import unittest
from random import shuffle

from balanced_bst import GenerateBBSTArray


class TestaBST(unittest.TestCase):
    def test_get_balanced_array(self) -> None:
        test_list = list(range(1, 8))
        shuffle(test_list)
        balanced_list = GenerateBBSTArray(test_list)
        self.assertListEqual(
            balanced_list,
            [4, 2, 6, 1, 3, 5, 7]
        )

    def test_get_balanced_array2(self) -> None:
        test_list = list(range(15))
        shuffle(test_list)
        balanced_list = GenerateBBSTArray(test_list)
        self.assertListEqual(
            balanced_list,
            [7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14]
        )

    def test_empty_array(self) -> None:
        test_list = []
        balances_list = GenerateBBSTArray(test_list)
        self.assertListEqual(balances_list, [])


if __name__ == '__main__':
    unittest.main()
