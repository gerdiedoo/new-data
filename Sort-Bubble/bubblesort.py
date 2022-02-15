def bubble_sort(input_array):
    '''Sort input_array using the brute force method of bubble sort

    Time Complexity (worst-case): O(n^2) - May need to iterate through up to n-1
    elements of the array up to n-1 times

    Space Complexity: O(1) - Only making modifications inside of input_array
    '''
    for i in range(len(input_array)-1):
        for pos in range(len(input_array)-1):
            if input_array[pos] > input_array[pos+1]:
                temp = input_array[pos]
                input_array[pos] = input_array[pos+1]
                input_array[pos+1] = temp
    return input_array

print(bubble_sort([21,4,1,3,9,20,25,6,21,14])) #[1,3,4,6,9,14,20,21,21,25]
print(bubble_sort([3,1,7,0,8])) #[0,1,3,7,8]
