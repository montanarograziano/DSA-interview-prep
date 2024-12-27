"""Implementations of common algorithms for Arrays."""


def binary_search(array: list[int], target: int) -> bool:
    """Binary Search implementation. The function searches for a target element in a sorted array.


    Args:
        array (list[int]): Array to search for the target element.
        target (int): Element to search for in the array.

    Returns:
        bool: True if the target element is found in the array, False otherwise.
    """

    left, right = 0, len(array)

    while left < right:
        mid = left + (right - left) // 2

        if array[mid] == target:
            return True
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid

    return False
