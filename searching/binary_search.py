"""
Binary Search

Problem: Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, return its index. Otherwise, return -1.

Time Complexity: O(log n)
Space Complexity: O(1)

Example:
    >>> search([−1, 0, 3, 5, 9, 12], 9)
    4
    >>> search([−1, 0, 3, 5, 9, 12], 13)
    -1
"""

def binary_search(nums, target):
    """
    Find target in sorted array using binary search.
    
    Args:
        nums (List[int]): Sorted list of integers
        target (int): Target value
    
    Returns:
        int: Index of target, or -1 if not found
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(nums, target, left=None, right=None):
    """
    Find target in sorted array using recursive binary search.
    
    Args:
        nums (List[int]): Sorted list of integers
        target (int): Target value
        left (int): Left boundary
        right (int): Right boundary
    
    Returns:
        int: Index of target, or -1 if not found
    """
    if left is None:
        left = 0
    if right is None:
        right = len(nums) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    else:
        return binary_search_recursive(nums, target, left, mid - 1)


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    print("Test 1:", binary_search(nums, 9))   # 4
    print("Test 2:", binary_search(nums, 13))  # -1
    print("Test 3:", binary_search(nums, -1))  # 0
    print("Test 4 (recursive):", binary_search_recursive(nums, 5))  # 3
