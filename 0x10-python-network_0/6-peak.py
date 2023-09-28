#!/usr/bin/python3
"""script for finding peak in list of ints
"""
def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.
    Args:
        list_of_integers (list): The list of unsorted integers.
    Returns:
        int: The peak element.
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # The peak is on the left side
            right = mid
        else:
            # The peak is on the right side
            left = mid + 1

    return list_of_integers[left]
