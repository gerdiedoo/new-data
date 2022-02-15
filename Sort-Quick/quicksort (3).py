"""Implement quick sort in Python.
Input a list.
Output a sorted list.

Implementation of quick sort found here: youtube.com/watch?v=SLauY6PpjW4

Time Complexity (best/average case): O(n*logn) - All n elements of the array
will typically have logn function calls made per element. The worst case (below)
should rarely occur in the real world if a smart random pivot (p) is selected.
Time Complexity (worst case): O(n^2) - In the rare worst case (e.g. if the
smallest or largest element in the input array is chosen for every function
call), there would be n function calls made for each of n elements.

Space Complexity: O(1) - No additional space is needed as all sorting is done
on the original array. Because quick sort requires no additional space and should
be time-efficient, it can be the first choice for solving many sorting problems.
"""
def quicksort(a):
    _quicksort(a, 0, len(a)-1)

def _quicksort(a, l, r):
    if l >= r:
        return
    i = partition(a,l,r)
    _quicksort(a,l,i-1)
    _quicksort(a,i,r)

def partition(a,l,r):
    p = a[(l+r)//2]
    while l <= r:
        while a[l] < p:
            l += 1
        while a[r] > p:
            r -= 1
        if l <= r:
            a[l],a[r] = a[r],a[l]
            l += 1
            r -= 1
    return l

test1 = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test2 = [8,3,1,7,0,10,2]
test3 = [10, 7, 8, 9, 1, 5]
test4 = [1,2,3]
quicksort(test1)
quicksort(test2)
quicksort(test3)
quicksort(test4)
print(test1) #[1,3,4,6,9,14,20,21,21,25]
print(test2) #[0,1,2,3,7,8.10]
print(test3) #[1,5,7,8,9,10]
print(test4) #[1,2,3]
