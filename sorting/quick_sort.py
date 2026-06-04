"""
Quick Sort

Problem: Sort an array of integers using quick sort algorithm.

Time Complexity: O(n log n) average, O(n²) worst case
Space Complexity: O(log n) due to recursion

Example:
    >>> quick_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]
    >>> quick_sort([5, 2, 8, 1, 9])
    [1, 2, 5, 8, 9]
"""

def quick_sort(arr):
    """
    Sort array using quick sort algorithm.
    
    Args:
        arr (List[int]): Unsorted list
    
    Returns:
        List[int]: Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr, left=0, right=None):
    """
    Sort array in-place using quick sort.
    
    Args:
        arr (List[int]): Array to sort
        left (int): Left boundary
        right (int): Right boundary
    
    Returns:
        List[int]: Sorted array
    """
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        pivot_index = partition(arr, left, right)
        quick_sort_inplace(arr, left, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, right)
    
    return arr


def partition(arr, left, right):
    """
    Partition array around pivot.
    
    Args:
        arr (List[int]): Array to partition
        left (int): Left boundary
        right (int): Right boundary
    
    Returns:
        int: Pivot index
    """
    pivot = arr[right]
    i = left - 1
    
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    print("Test 1:", quick_sort([64, 34, 25, 12, 22, 11, 90]))  # [11, 12, 22, 25, 34, 64, 90]
    print("Test 2:", quick_sort([5, 2, 8, 1, 9]))               # [1, 2, 5, 8, 9]
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Test 3 (in-place):", quick_sort_inplace(arr))         # [11, 12, 22, 25, 34, 64, 90]
