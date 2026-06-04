"""
Valid Palindrome

Problem: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters 
include letters and numbers.

Time Complexity: O(n)
Space Complexity: O(1)

Example:
    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("race a car")
    False
    >>> is_palindrome(" ")
    True
"""

def is_palindrome(s):
    """
    Check if string is palindrome using two pointers.
    
    Args:
        s (str): Input string
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    
    return True


def is_palindrome_simple(s):
    """
    Simple approach: clean string and check.
    
    Args:
        s (str): Input string
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    clean = ''.join(char.lower() for char in s if char.isalnum())
    return clean == clean[::-1]


if __name__ == "__main__":
    print("Test 1:", is_palindrome("A man, a plan, a canal: Panama"))  # True
    print("Test 2:", is_palindrome("race a car"))                      # False
    print("Test 3:", is_palindrome(" "))                              # True
    print("Test 4 (simple):", is_palindrome_simple("0P"))             # False
