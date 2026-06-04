"""
Longest Substring Without Repeating Characters

Problem: Given a string s, find the length of the longest substring without repeating characters.

Time Complexity: O(n)
Space Complexity: O(min(m, n)) where m is charset size

Example:
    >>> length_of_longest_substring("abcabcbb")
    3  # "abc"
    >>> length_of_longest_substring("bbbbb")
    1  # "b"
    >>> length_of_longest_substring("pwwkew")
    3  # "wke"
"""

def length_of_longest_substring(s):
    """
    Find length of longest substring without repeating characters using sliding window.
    
    Args:
        s (str): Input string
    
    Returns:
        int: Length of longest substring
    """
    char_index = {}
    max_length = 0
    start = 0
    
    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1
        
        char_index[s[end]] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length


def longest_substring_without_repeating(s):
    """
    Find the actual longest substring without repeating characters.
    
    Args:
        s (str): Input string
    
    Returns:
        str: Longest substring
    """
    char_index = {}
    max_length = 0
    start = 0
    max_start = 0
    
    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1
        
        char_index[s[end]] = end
        
        if end - start + 1 > max_length:
            max_length = end - start + 1
            max_start = start
    
    return s[max_start:max_start + max_length]


if __name__ == "__main__":
    print("Test 1:", length_of_longest_substring("abcabcbb"))  # 3
    print("Test 2:", length_of_longest_substring("bbbbb"))     # 1
    print("Test 3:", length_of_longest_substring("pwwkew"))    # 3
    print("Test 4 (substring):", longest_substring_without_repeating("abcabcbb"))  # "abc"
