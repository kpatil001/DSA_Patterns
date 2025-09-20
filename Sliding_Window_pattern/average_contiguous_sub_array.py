# In many problems dealing with an array (or a LinkedList), we are asked to find or calculate something among all the contiguous subarrays (or sublists) of a given size. For example, take a look at this problem:

# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

# Let’s understand this problem with a real input:

# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# Here, we are asked to find the average of all contiguous subarrays of size ‘5’ in the given array. Let’s solve this:

def average_contiguous_subarray(array,size):
    
    index = 0
    sum = 0
    element_before_window_index = 0
    result = []
    while index < len(array):
        sum += array[index]
        if index >= size - 1:
            result.append(sum/size)
            sum -= array[element_before_window_index]
            element_before_window_index += 1
        index += 1    

    return result

if __name__ == "__main__":
    print(average_contiguous_subarray([1,2,3,6,-1,4,1,8,2],5))