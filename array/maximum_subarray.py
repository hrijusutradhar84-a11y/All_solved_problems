"""
Maximum Subarray Problem (Kadane's Algorithm)

Problem: Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return that sum.

Time Complexity: O(n)
Space Complexity: O(1)

Example:
    >>> max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6  # [4, -1, 2, 1]
    >>> max_subarray([5, 4, -1, 7, 8])
    23  # entire array
"""

def max_subarray(nums):
    """
    Find maximum sum of contiguous subarray using Kadane's algorithm.
    
    Args:
        nums (List[int]): List of integers
    
    Returns:
        int: Maximum sum
    """
    max_current = max_global = nums[0]
    
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        max_global = max(max_global, max_current)
    
    return max_global


def max_subarray_with_indices(nums):
    """
    Find maximum sum and return the subarray indices.
    
    Args:
        nums (List[int]): List of integers
    
    Returns:
        tuple: (max_sum, start_index, end_index)
    """
    max_current = max_global = nums[0]
    start = end = temp_start = 0
    
    for i in range(1, len(nums)):
        if nums[i] > max_current + nums[i]:
            max_current = nums[i]
            temp_start = i
        else:
            max_current = max_current + nums[i]
        
        if max_current > max_global:
            max_global = max_current
            start = temp_start
            end = i
    
    return max_global, start, end, nums[start:end+1]


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Test 1:", max_subarray(arr))  # 6
    print("Test 2:", max_subarray([5, 4, -1, 7, 8]))  # 23
    result = max_subarray_with_indices(arr)
    print("Test 3 (with indices):", result)  # (6, 3, 6, [4, -1, 2, 1])
