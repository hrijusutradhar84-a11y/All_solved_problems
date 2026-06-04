"""
Fibonacci Number

Problem: Given an integer n, return the nth Fibonacci number. The Fibonacci sequence is defined as:
F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1.

Time Complexity: O(n) for DP, O(2^n) for naive recursion
Space Complexity: O(n) for DP, O(1) for optimized

Example:
    >>> fib(4)
    3
    >>> fib(10)
    55
"""

def fib_recursive(n):
    """
    Calculate nth Fibonacci using naive recursion (inefficient).
    
    Args:
        n (int): Position in Fibonacci sequence
    
    Returns:
        int: nth Fibonacci number
    """
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_memo(n, memo=None):
    """
    Calculate nth Fibonacci using memoization.
    
    Args:
        n (int): Position in Fibonacci sequence
        memo (dict): Memoization dictionary
    
    Returns:
        int: nth Fibonacci number
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_dp(n):
    """
    Calculate nth Fibonacci using dynamic programming (bottom-up).
    
    Args:
        n (int): Position in Fibonacci sequence
    
    Returns:
        int: nth Fibonacci number
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def fib_optimized(n):
    """
    Calculate nth Fibonacci with O(1) space optimization.
    
    Args:
        n (int): Position in Fibonacci sequence
    
    Returns:
        int: nth Fibonacci number
    """
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr


if __name__ == "__main__":
    print("Test 1 (memo):", fib_memo(10))       # 55
    print("Test 2 (DP):", fib_dp(10))           # 55
    print("Test 3 (optimized):", fib_optimized(10))  # 55
    print("Test 4 (memo):", fib_memo(6))        # 8
