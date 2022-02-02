
# Best case: O(nlog(n))
# Average case: O(nlog(n))
# Worse case: O(n^2)


class QuickSort:
    def __init__(self):
        self.name = "Quick Sort"
    @staticmethod
    def quickSort(arr, start, end):
        pivot = arr[end]
        i = start-1
        for x in range(start, end):
            if arr[x] > pivot:
                continue
            else:
                i += 1
                arr[i],arr[x] = arr[x],arr[i]
        for y in range(end, i + 1, -1):
            arr[y] = arr[y-1]
        arr[i + 1] = pivot
        return arr.index(pivot)
    @staticmethod
    def partition(array, start, end):
        if start < end:                       # this is enough to end recursion
            pos = QuickSort.quickSort(array, start, end)
            QuickSort.partition(array, start, pos - 1)
            QuickSort.partition(array, pos + 1, end)



test = QuickSort()
array = [7, 2, 1, 8, 6, 3, 5, 4]
test.partition(array, 0, 7)
print(array)