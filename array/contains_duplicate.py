"""
Contains Duplicate Problem

Problem: Given an integer array nums, return True if any value appears at least twice in the array, 
and return False if every element is distinct.

Time Complexity: O(n)
Space Complexity: O(n)

Example:
    >>> contains_duplicate([1, 2, 3, 1])
    True
    >>> contains_duplicate([1, 2, 3, 4])
    False
"""

def contains_duplicate(nums):
    """
    Check if array contains duplicates using set.
    
    Args:
        nums (List[int]): List of integers
    
    Returns:
        bool: True if duplicate exists, False otherwise
    """
    return len(nums) != len(set(nums))


def contains_duplicate_optimized(nums):
    """
    Early exit optimization - returns as soon as duplicate found.
    
    Args:
        nums (List[int]): List of integers
    
    Returns:
        bool: True if duplicate exists, False otherwise
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    print("Test 1:", contains_duplicate([1, 2, 3, 1]))      # True
    print("Test 2:", contains_duplicate([1, 2, 3, 4]))      # False
    print("Test 3:", contains_duplicate_optimized([99, 99])) # True
