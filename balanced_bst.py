from typing import List


def GenerateBBSTArray(a: List[int]) -> List[int]:
    if not a:
        return []

    a.sort()
    balanced_array = len(a) * [0]
    _generate_bst_array(a, balanced_array, 0)
    return balanced_array


def _generate_bst_array(array: List[int],
                        balanced_array: List[int],
                        index: int) -> None:
    """Recursively return left / right root's children"""

    if not array:
        return None

    mid = len(array) // 2
    balanced_array[index] = array[mid]

    # left ancestor
    _generate_bst_array(array[:mid], balanced_array, index * 2 + 1)
    # right ancestor
    _generate_bst_array(array[mid + 1:], balanced_array, index * 2 + 2)
