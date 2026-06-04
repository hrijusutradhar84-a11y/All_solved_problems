"""
Factorial

Problem: Calculate the factorial of a non-negative integer n. The factorial of n (denoted as n!) is 
the product of all positive integers less than or equal to n.

Time Complexity: O(n)
Space Complexity: O(n) for recursion, O(1) for iterative

Example:
    >>> factorial(5)
    120  # 5! = 5 × 4 × 3 × 2 × 1
    >>> factorial(0)
    1    # By definition
"""

def factorial_recursive(n):
    """
    Calculate factorial using recursion.
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: Factorial of n
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    """
    Calculate factorial using iteration.
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: Factorial of n
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


def factorial_memo(n, memo=None):
    """
    Calculate factorial using memoization.
    
    Args:
        n (int): Non-negative integer
        memo (dict): Memoization dictionary
    
    Returns:
        int: Factorial of n
    """
    if memo is None:
        memo = {}
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n in memo:
        return memo[n]
    
    if n == 0 or n == 1:
        return 1
    
    memo[n] = n * factorial_memo(n - 1, memo)
    return memo[n]


if __name__ == "__main__":
    print("Test 1 (recursive):", factorial_recursive(5))    # 120
    print("Test 2 (recursive):", factorial_recursive(0))    # 1
    print("Test 3 (iterative):", factorial_iterative(5))    # 120
    print("Test 4 (iterative):", factorial_iterative(10))   # 3628800
    print("Test 5 (memo):", factorial_memo(7))              # 5040
