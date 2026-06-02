"""
Two Sum Problem

Given an array of integers nums and an integer target, return the indices of the two numbers
that add up to target. You may assume that each input has exactly one solution, and you may
not use the same element twice.

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: nums[0] + nums[1] == 9, so we return [0, 1].

Time Complexity: O(n) - single pass with hash map
Space Complexity: O(n) - hash map storage
"""


def two_sum(nums, target):
    """
    Find two numbers in array that sum to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List containing indices of two numbers
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    # Test cases
    print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(two_sum([3, 2, 4], 6))       # Output: [1, 2]
    print(two_sum([3, 3], 6))          # Output: [0, 1]
