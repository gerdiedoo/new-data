"""You're going to write a binary search function.
You should use a recursive approach - meaning
binary_search will call itself to return a value.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value, high, low):
    if high >= low:
        mid = (high+low)//2
        if value == input_array[mid]:
            return mid
        elif value > input_array[mid]:
            return binary_search(input_array, value, high, mid+1)
        else:
            return binary_search(input_array, value, mid-1, low)
    else:
        return -1


test_list = [1,3,9,11,15,17,19,29]
test_val1 = 25
test_val2 = 15
test_val3 = 17
print(binary_search(test_list, test_val1, len(test_list)-1, 0)) #-1
print(binary_search(test_list, test_val2, len(test_list)-1, 0)) #4
print(binary_search(test_list, test_val3, len(test_list)-1, 0)) #5
