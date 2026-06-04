"""
Merge Sort

Problem: Sort an array of integers using merge sort algorithm.

Time Complexity: O(n log n) in all cases
Space Complexity: O(n)

Example:
    >>> merge_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]
    >>> merge_sort([5, 2, 8, 1, 9])
    [1, 2, 5, 8, 9]
"""

def merge_sort(arr):
    """
    Sort array using merge sort algorithm.
    
    Args:
        arr (List[int]): Unsorted list
    
    Returns:
        List[int]: Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """
    Merge two sorted arrays.
    
    Args:
        left (List[int]): First sorted array
        right (List[int]): Second sorted array
    
    Returns:
        List[int]: Merged sorted array
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


if __name__ == "__main__":
    print("Test 1:", merge_sort([64, 34, 25, 12, 22, 11, 90]))  # [11, 12, 22, 25, 34, 64, 90]
    print("Test 2:", merge_sort([5, 2, 8, 1, 9]))               # [1, 2, 5, 8, 9]
    print("Test 3:", merge_sort([1]))                           # [1]
    print("Test 4:", merge_sort([]))                            # []
