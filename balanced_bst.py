from typing import List


def GenerateBBSTArray(a: List[int]) -> List[int]:
    if not a:
        return []

    a.sort()
    root = _get_root(a)
    return [root] + _generate_bbst_array(a)


def _generate_bbst_array(array: List[int]) -> List[int]:
    """Recursivly return left / right root's children"""

    mid = len(array) // 2
    if mid < 2:
        return []

    left_array = array[:mid]
    right_array = array[mid:]

    left_child = _get_root(left_array)
    right_child = _get_root(right_array)

    return (
        [left_child, right_child]
        + _generate_bbst_array(array[:mid])
        + _generate_bbst_array(array[mid:])
    )


def _get_root(array: List[int]) -> int:
    """Return root as center element of array"""

    return array[len(array) // 2]
