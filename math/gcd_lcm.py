"""
Greatest Common Divisor (GCD) and Least Common Multiple (LCM)

Problem: Find GCD and LCM of two or more numbers.

Time Complexity: O(log(min(a, b))) for Euclidean algorithm
Space Complexity: O(1)

Example:
    >>> gcd(12, 8)
    4
    >>> lcm(12, 8)
    24
    >>> gcd_multiple([12, 18, 24])
    6
"""

def gcd(a, b):
    """
    Find GCD of two numbers using Euclidean algorithm.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: GCD of a and b
    """
    while b:
        a, b = b, a % b
    return a


def gcd_recursive(a, b):
    """
    Find GCD using recursion.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: GCD of a and b
    """
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def lcm(a, b):
    """
    Find LCM of two numbers.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: LCM of a and b
    """
    return abs(a * b) // gcd(a, b)


def gcd_multiple(numbers):
    """
    Find GCD of multiple numbers.
    
    Args:
        numbers (list): List of integers
    
    Returns:
        int: GCD of all numbers
    """
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result


def lcm_multiple(numbers):
    """
    Find LCM of multiple numbers.
    
    Args:
        numbers (list): List of integers
    
    Returns:
        int: LCM of all numbers
    """
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result


if __name__ == "__main__":
    print("Test 1 (GCD):", gcd(12, 8))              # 4
    print("Test 2 (GCD recursive):", gcd_recursive(12, 8))  # 4
    print("Test 3 (LCM):", lcm(12, 8))              # 24
    print("Test 4 (GCD multiple):", gcd_multiple([12, 18, 24]))  # 6
    print("Test 5 (LCM multiple):", lcm_multiple([12, 8, 16])) # 48
