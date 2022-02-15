import math
def binarySearch(array, target):
	leftpointer = 0
	rightpointer = len(array) - 1
    while rightpointer > leftpointer:
    	if array[leftpointer] == target:
    		return leftpointer
    	if array[rightpointer] == target:
    		return rightpointer	
		pivot = math.floor((leftpointer + rightpointer)/2)
    
		if array[pivot] == target:
			return pivot
		elif array[pivot] > target:
			rightpointer = pivot -1
	
		else :
			leftpointer = pivot +1
	
	return -1