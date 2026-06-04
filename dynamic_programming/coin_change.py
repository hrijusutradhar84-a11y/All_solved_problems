"""
Coin Change Problem

Problem: You are given an integer array coins representing coins of different denominations and an integer 
amount representing a total amount of money. Return the fewest number of coins that you need to make up that 
amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Time Complexity: O(amount * len(coins))
Space Complexity: O(amount)

Example:
    >>> coin_change([1, 2, 5], 5)
    1  # 5 = 5
    >>> coin_change([2], 3)
    -1
    >>> coin_change([10], 10)
    1  # 10 = 10
"""

def coin_change(coins, amount):
    """
    Find minimum number of coins to make the amount using DP.
    
    Args:
        coins (List[int]): List of coin denominations
        amount (int): Target amount
    
    Returns:
        int: Minimum number of coins, or -1 if impossible
    """
    # dp[i] represents minimum coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_with_coins(coins, amount):
    """
    Find minimum coins and return which coins to use.
    
    Args:
        coins (List[int]): List of coin denominations
        amount (int): Target amount
    
    Returns:
        tuple: (min_coins, coins_used) or (-1, [])
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin
    
    if dp[amount] == float('inf'):
        return -1, []
    
    # Reconstruct the coins used
    result = []
    current = amount
    while current > 0:
        coin = parent[current]
        result.append(coin)
        current -= coin
    
    return dp[amount], result


if __name__ == "__main__":
    print("Test 1:", coin_change([1, 2, 5], 5))      # 1
    print("Test 2:", coin_change([2], 3))             # -1
    print("Test 3:", coin_change([10], 10))           # 1
    print("Test 4:", coin_change([1, 3, 4], 6))       # 2
    result, used = coin_change_with_coins([1, 2, 5], 5)
    print("Test 5 (with coins):", result, "coins:", used)  # (1, [5])
