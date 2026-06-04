"""
Bubble Sort

Problem: Sort an array of integers using bubble sort algorithm.

Time Complexity: O(n²) worst and average case, O(n) best case
Space Complexity: O(1)

Example:
    >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]
    >>> bubble_sort([5, 2, 8, 1, 9])
    [1, 2, 5, 8, 9]
"""

def bubble_sort(arr):
    """
    Sort array using bubble sort algorithm.
    
    Args:
        arr (List[int]): Unsorted list
    
    Returns:
        List[int]: Sorted list
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr


def bubble_sort_verbose(arr):
    """
    Bubble sort with step-by-step output.
    
    Args:
        arr (List[int]): Unsorted list
    
    Returns:
        List[int]: Sorted list
    """
    n = len(arr)
    print(f"Initial array: {arr}")
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        print(f"Pass {i + 1}: {arr}")
        
        if not swapped:
            break
    
    return arr


if __name__ == "__main__":
    print("Test 1:", bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # [11, 12, 22, 25, 34, 64, 90]
    print("\nTest 2 (verbose):")
    bubble_sort_verbose([5, 2, 8, 1, 9])
