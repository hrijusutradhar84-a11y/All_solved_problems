"""
Find First and Last Position of Element in Sorted Array

Problem: Given an array of integers nums sorted in non-decreasing order, find the starting and ending 
position of a given target value. If target is not found in the array, return [-1, -1].

Time Complexity: O(log n)
Space Complexity: O(1)

Example:
    >>> searchRange([5, 7, 7, 8, 8, 10], 8)
    [3, 4]
    >>> searchRange([5, 7, 7, 8, 8, 10], 6)
    [-1, -1]
"""

def searchRange(nums, target):
    """
    Find first and last position of target using binary search.
    
    Args:
        nums (List[int]): Sorted list of integers
        target (int): Target value
    
    Returns:
        List[int]: [first_position, last_position] or [-1, -1]
    """
    def find_first(nums, target):
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    def find_last(nums, target):
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    if not nums:
        return [-1, -1]
    
    first = find_first(nums, target)
    if first == -1:
        return [-1, -1]
    
    last = find_last(nums, target)
    return [first, last]


if __name__ == "__main__":
    print("Test 1:", searchRange([5, 7, 7, 8, 8, 10], 8))   # [3, 4]
    print("Test 2:", searchRange([5, 7, 7, 8, 8, 10], 6))   # [-1, -1]
    print("Test 3:", searchRange([], 0))                     # [-1, -1]
    print("Test 4:", searchRange([1], 1))                    # [0, 0]
