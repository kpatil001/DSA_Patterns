# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

# Example 1:

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

# Example 2:

# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].


def subarray_with_max_sum(array,size):

    sum = 0
    max = -9999
    window_start = 0
    max_sum_window_start = 0
    for index in range(len(array)):
        sum += array[index]
        if index >= size - 1:
            if sum > max:
                max_sum_window_start = window_start
                max = sum
            sum -= array[window_start]
            window_start += 1

    return array[max_sum_window_start:max_sum_window_start+size]

if __name__ == '__main__':
    print(subarray_with_max_sum([2, 3, 4,4, 1, 5],2))