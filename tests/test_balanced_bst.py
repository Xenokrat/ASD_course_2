import unittest
from random import shuffle

from balanced_bst import GenerateBBSTArray


class TestaBST(unittest.TestCase):
    def test_get_balanced_array(self) -> None:
        test_list = list(range(1, 8))
        shuffle(test_list)
        balances_list = GenerateBBSTArray(test_list)
        self.assertListEqual(balances_list, [4, 2, 6, 1, 3, 5, 7])

    def test_get_balanced_array2(self) -> None:
        test_list = [37, 55, 62, 50, 25, 15, 22, 92, 80, 84, 68, 31, 75, 43]
        balances_list = GenerateBBSTArray(test_list)
        self.assertListEqual(
            balances_list,
            [50, 25, 75, 20, 37, 62, 84, 15, 22, 31, 43, 55, 68, 80, 92]
        )

    def test_empty_array(self) -> None:
        test_list = []
        balances_list = GenerateBBSTArray(test_list)
        self.assertListEqual(balances_list, [])


if __name__ == '__main__':
    unittest.main()
