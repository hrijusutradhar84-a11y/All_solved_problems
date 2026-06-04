"""
Product of Array Except Self

Problem: Given an integer array nums, return an array answer such that answer[i] is equal to the product 
of all the elements of nums except nums[i]. You must write an algorithm that runs in O(n) time and without 
using the division operation.

Time Complexity: O(n)
Space Complexity: O(1) excluding output array

Example:
    >>> product_except_self([1, 2, 3, 4])
    [24, 12, 8, 6]
    >>> product_except_self([2, 3, 4, 5])
    [60, 40, 30, 24]
"""

def product_except_self(nums):
    """
    Calculate product of array except self using prefix/suffix products.
    
    Args:
        nums (List[int]): List of integers
    
    Returns:
        List[int]: Products of all except self
    """
    n = len(nums)
    answer = [1] * n
    
    # Calculate prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
    
    # Calculate suffix products and multiply with prefix
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    
    return answer


if __name__ == "__main__":
    print("Test 1:", product_except_self([1, 2, 3, 4]))    # [24, 12, 8, 6]
    print("Test 2:", product_except_self([2, 3, 4, 5]))    # [60, 40, 30, 24]
    print("Test 3:", product_except_self([-1, 1, 0, -3, 3])) # [0, 0, 9, 0, 0]
