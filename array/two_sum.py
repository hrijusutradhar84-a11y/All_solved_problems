"""
Two Sum Problem

Problem: Given an array of integers nums and an integer target, return the indices of the two numbers 
that add up to the target. You may assume each input has exactly one solution, and you cannot use the 
same element twice.

Time Complexity: O(n)
Space Complexity: O(n)

Example:
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]
    >>> two_sum([3, 2, 4], 6)
    [1, 2]
"""

def two_sum(nums, target):
    """
    Find two numbers that add up to target using hash map.
    
    Args:
        nums (List[int]): List of integers
        target (int): Target sum
    
    Returns:
        List[int]: Indices of two numbers
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    print("Test 1:", two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print("Test 2:", two_sum([3, 2, 4], 6))        # [1, 2]
    print("Test 3:", two_sum([3, 3], 6))           # [0, 1]
