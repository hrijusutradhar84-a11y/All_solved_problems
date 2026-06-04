"""
Best Time to Buy and Sell Stock

Problem: You are given an array prices where prices[i] is the price of a given stock on the ith day. 
You want to maximize your profit by choosing a single day to buy one stock and choosing a different 
day in the future to sell that stock. Return the maximum profit you can achieve. If no profit is 
possible, return 0.

Time Complexity: O(n)
Space Complexity: O(1)

Example:
    >>> max_profit([7, 1, 5, 3, 6, 4])
    5  # Buy at 1, sell at 6
    >>> max_profit([7, 6, 4, 3, 1])
    0  # No profit possible
"""

def max_profit(prices):
    """
    Find maximum profit from single buy-sell transaction.
    
    Args:
        prices (List[int]): List of stock prices
    
    Returns:
        int: Maximum profit
    """
    if not prices or len(prices) < 2:
        return 0
    
    min_price = prices[0]
    max_profit_val = 0
    
    for price in prices[1:]:
        profit = price - min_price
        max_profit_val = max(max_profit_val, profit)
        min_price = min(min_price, price)
    
    return max_profit_val


def max_profit_with_details(prices):
    """
    Find maximum profit and return buy/sell days.
    
    Args:
        prices (List[int]): List of stock prices
    
    Returns:
        tuple: (max_profit, buy_day, sell_day)
    """
    if not prices or len(prices) < 2:
        return 0, -1, -1
    
    min_price = prices[0]
    min_day = 0
    max_profit_val = 0
    sell_day = -1
    
    for i in range(1, len(prices)):
        profit = prices[i] - min_price
        if profit > max_profit_val:
            max_profit_val = profit
            sell_day = i
        if prices[i] < min_price:
            min_price = prices[i]
            min_day = i
    
    return max_profit_val, min_day, sell_day


if __name__ == "__main__":
    print("Test 1:", max_profit([7, 1, 5, 3, 6, 4]))  # 5
    print("Test 2:", max_profit([7, 6, 4, 3, 1]))     # 0
    print("Test 3:", max_profit([2, 4, 1, 7, 5, 11])) # 10
    print("Test 4 (with details):", max_profit_with_details([7, 1, 5, 3, 6, 4]))  # (5, 1, 4)
