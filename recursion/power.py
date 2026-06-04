"""
Power Function (x^n)

Problem: Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Time Complexity: O(log n) for optimized, O(n) for naive
Space Complexity: O(log n) for recursion, O(1) for iterative

Example:
    >>> power(2.0, 10)
    1024.0
    >>> power(2.0, -2)
    0.25
    >>> power(2.0, 0)
    1.0
"""

def power_naive(x, n):
    """
    Calculate x^n using naive approach.
    
    Args:
        x (float): Base
        n (int): Exponent
    
    Returns:
        float: x raised to power n
    """
    if n == 0:
        return 1.0
    if n < 0:
        return 1 / power_naive(x, -n)
    
    result = 1
    for _ in range(n):
        result *= x
    
    return result


def power_optimized(x, n):
    """
    Calculate x^n using fast exponentiation (binary exponentiation).
    
    Args:
        x (float): Base
        n (int): Exponent
    
    Returns:
        float: x raised to power n
    """
    if n == 0:
        return 1.0
    
    if n < 0:
        x = 1 / x
        n = -n
    
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2
    
    return result


def power_recursive(x, n):
    """
    Calculate x^n using recursive fast exponentiation.
    
    Args:
        x (float): Base
        n (int): Exponent
    
    Returns:
        float: x raised to power n
    """
    if n == 0:
        return 1.0
    
    if n < 0:
        return 1 / power_recursive(x, -n)
    
    if n % 2 == 0:
        half = power_recursive(x, n // 2)
        return half * half
    else:
        return x * power_recursive(x, n - 1)


if __name__ == "__main__":
    print("Test 1 (naive):", power_naive(2.0, 10))       # 1024.0
    print("Test 2 (optimized):", power_optimized(2.0, 10))     # 1024.0
    print("Test 3 (optimized):", power_optimized(2.0, -2))     # 0.25
    print("Test 4 (recursive):", power_recursive(2.0, 10))     # 1024.0
    print("Test 5 (recursive):", power_recursive(2.0, -2))     # 0.25
