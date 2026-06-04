"""
Climbing Stairs

Problem: You are climbing a staircase. It takes n steps to reach the top. Each time you can climb 1 or 2 
steps. In how many distinct ways can you climb to the top?

Time Complexity: O(n)
Space Complexity: O(n) for DP, O(1) for optimized

Example:
    >>> climb_stairs(3)
    3  # 1+1+1, 1+2, 2+1
    >>> climb_stairs(4)
    5  # 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2
"""

def climb_stairs_recursive(n):
    """
    Count ways to climb stairs using recursion (inefficient).
    
    Args:
        n (int): Number of stairs
    
    Returns:
        int: Number of distinct ways
    """
    if n <= 2:
        return n
    return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)


def climb_stairs_dp(n):
    """
    Count ways to climb stairs using DP.
    
    Args:
        n (int): Number of stairs
    
    Returns:
        int: Number of distinct ways
    """
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def climb_stairs_optimized(n):
    """
    Count ways to climb stairs with O(1) space.
    
    Args:
        n (int): Number of stairs
    
    Returns:
        int: Number of distinct ways
    """
    if n <= 2:
        return n
    
    prev1, prev2 = 2, 1
    
    for _ in range(3, n + 1):
        prev1, prev2 = prev1 + prev2, prev1
    
    return prev1


if __name__ == "__main__":
    print("Test 1 (DP):", climb_stairs_dp(3))        # 3
    print("Test 2 (DP):", climb_stairs_dp(4))        # 5
    print("Test 3 (optimized):", climb_stairs_optimized(5))  # 8
    print("Test 4 (optimized):", climb_stairs_optimized(10)) # 89
