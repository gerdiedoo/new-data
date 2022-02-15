"""Implement a bubble sort algorithm."""


def bubble_sort(arr):
    """Sort iterable from smallest to largest."""
    l = len(arr)
    for i in range(l):
        for i in range(l - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr
