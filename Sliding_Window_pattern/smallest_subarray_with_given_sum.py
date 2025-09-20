# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

# Example 1:

# Input: [2, 1, 5, 2, 3, 2], S=7 
# Output: 2
# Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
# Example 2:

# Input: [2, 1, 5, 2, 8], S=7 
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
# Example 3:

# Input: [3, 4, 1, 1, 6], S=8 
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

#this is one way of implementation
def smallest_subarray_with_given_sum_one_loop(array,target):
    begin_index = end_index = sum = smallest_subarray_begin_index = smallest_subarray_end_index= 0
    smallest_subarray_length = len(array)
    sum = array[0]
    while begin_index < len(array):
        if sum >= target:
            subarray_length = (end_index - begin_index) + 1
            if subarray_length < smallest_subarray_length:
                smallest_subarray_begin_index = begin_index
                smallest_subarray_end_index = end_index
                smallest_subarray_length = subarray_length
            sum -= array[begin_index]
            begin_index += 1
        elif end_index < len(array) - 1:
            end_index += 1
            sum += array[end_index]
        else:
            break
    return smallest_subarray_length, array[smallest_subarray_begin_index:smallest_subarray_end_index+1]
#Time complexity is O(n) as at max begin index moves from start to end and same does the end index and at every iteration either of the index move ahead by one
#hence max iterations are n+n = 2n hence complexity is of O(n)

import math
# this is more simplified version of solution with same time complexity
def smallest_subarray_with_given_sum_simplefied(array,target):
    begin_index = window_sum = 0
    min_window_length = math.inf
    smallest_subarray_begin_index = smallest_subarray_end_index = 0

    for end_index in range(len(array)):
        window_sum += array[end_index]

        while window_sum >= target:
            subarray_length = end_index - begin_index + 1
            if subarray_length < min_window_length:
                smallest_subarray_begin_index = begin_index
                smallest_subarray_end_index = end_index
                min_window_length = subarray_length
            window_sum -= array[begin_index]
            begin_index += 1
        
    if min_window_length == math.inf:
        return 0,[]
    else:
        return min_window_length,array[smallest_subarray_begin_index:smallest_subarray_end_index+1]
            


if __name__ == '__main__':
    print(smallest_subarray_with_given_sum_one_loop([3, 4, 1, 1, 6],8))
    print(smallest_subarray_with_given_sum_simplefied([3, 4, 1, 1, 6],8))


