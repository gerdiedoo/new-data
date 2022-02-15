# Time complexity
# Worst case --> O(n^2)
# Average case --> O(n^2)


def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        key = arr[j]
        while j > 0 and key < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = key
    return arr
