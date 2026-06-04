"""
Reverse String

Problem: Write a function that reverses a string. The input string is given as an array of characters s.

Time Complexity: O(n)
Space Complexity: O(1) if in-place, O(n) otherwise

Example:
    >>> reverse_string(['h', 'e', 'l', 'l', 'o'])
    ['o', 'l', 'l', 'e', 'h']
    >>> reverse_string(['H', 'a', 'n', 'n', 'a', 'h'])
    ['h', 'a', 'n', 'n', 'a', 'H']
"""

def reverse_string(s):
    """
    Reverse string in-place using two pointers.
    
    Args:
        s (List[str]): Character array
    
    Returns:
        None (modifies in-place)
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverse_string_copy(s):
    """
    Reverse string and return new array.
    
    Args:
        s (List[str]): Character array
    
    Returns:
        List[str]: Reversed string
    """
    return s[::-1]


if __name__ == "__main__":
    s1 = ['h', 'e', 'l', 'l', 'o']
    reverse_string(s1)
    print("Test 1:", s1)  # ['o', 'l', 'l', 'e', 'h']
    
    s2 = ['H', 'a', 'n', 'n', 'a', 'h']
    reverse_string(s2)
    print("Test 2:", s2)  # ['h', 'a', 'n', 'n', 'a', 'H']
    
    print("Test 3 (copy):", reverse_string_copy(['a', 'b', 'c']))  # ['c', 'b', 'a']
