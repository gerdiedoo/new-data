"""
# 4,2,1,5,3
# 2,4,[1],5,3 lastSortedIdx = 1
# 1,2,4,[5],3 lastSortedIdx = 2
In place sorting 
"""
def insertsort(A):
    """
    Loop invariant: all items before i that's in current for loop are sorted
    efficient when most of items are already in sorted position

    Time: O(n^2) upper bound if in reverse order
    Space: O(1)
    """
    _len = len(A)
    if _len <= 1:
        return A
    for i in xrange(1, _len):
        j = i
        while A[j] < A[j-1] and j > 0:
            # since items up to i-1 have been sorted, if A[j] is in right position
            # we could early break go to next one to check
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
    return A

"""
# 4 1 2 5 3
In place sorting
"""
def selectsort(A):
    for i in xrange(len(A)):
        # initial min index is current i, items before i are sorted
        minIdx = i
        # select the min index after i
        for j in xrange(i+1, len(A)):
            if A[j] < A[minIdx]:
            # not swap here as bubble sort, just update min index
                minIdx = j
        A[i], A[minIdx] = A[minIdx], A[i]
    
"""
Time: O(NlogN)
Space: O(N) or use in place merge for two divided arrays
"""
def mergesort(A):
    def divide(A, l, r):
        print l, r
        if (l >= r):
            return [A[r]]
        m = (l + r) / 2
        L = divide(A, l, m)
        R = divide(A, m+1, r)

        return merge_(L, R)

    # merge does the actual work, since two parts are sorted
    # avoid the comparison between every two items
    def merge_(L, R):
        lenL, lenR = len(L), len(R)
        i, j = 0, 0
        r = []
        while i < lenL and j < lenR:
            if L[i] < R[j]:
                r.append(L[i])
                i += 1
            else:
                r.append(R[j])
                j += 1
        while i < lenL:
            r.append(L[i])
            i += 1
        while j < lenR:
            r.append(R[j])
            j += 1
    
        return r
    
    return divide(A, 0, len(A)-1)

    
if __name__ == '__main__':
    A = [1,3,35,5,4, 6]
    # A = [4,1,2,5,3]
    B = [6,6,6,6,6,6,6,6,6,6]
    # print insertsort(A)
    # selectsort(A)
    res = mergesort(B)
    print res
