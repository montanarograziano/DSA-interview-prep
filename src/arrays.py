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


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums

    mid = len(nums) // 2

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(nums, left, right)


def merge(nums, left, right):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
            k += 1
        else:
            nums[k] = right[j]
            j += 1
            k += 1

    nums[k:] = left[i:] if i < len(left) else right[j:]

    return nums
