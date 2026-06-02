"""
Increasing and Decreasing Numbers

An increasing number has digits that never decrease when read left to right.
Example: 234559 is increasing.

A decreasing number has digits where no digit is bigger than the previous one.
Example: 97732 is decreasing.

All single and two-digit numbers (00-99) are either increasing or decreasing.
101 is the first number that is neither.

Task: Return the total count of all increasing or decreasing numbers below 10^x.

Examples:
    x = 0 → 1
    x = 1 → 10 (0-9)
    x = 2 → 100 (0-99)
    x = 3 → 475
    x = 4 → 1675
    x = 5 → 4954
    x = 6 → 12952

Time Complexity: O(1) - Direct mathematical formula using combinatorics
Space Complexity: O(1) - Only uses a few variables
"""

import math


def total_inc_dec(x):
    """
    Calculate total count of increasing and decreasing numbers below 10^x.

    The solution uses combinatorics:
    - Increasing numbers: C(x+9, 9) - selections of digits in non-decreasing order
    - Decreasing numbers: C(x+10, 10) - x - selections of digits in non-increasing order
    - Common numbers: 9*x + 1 - numbers that are both increasing and decreasing

    Args:
        x: Power of 10 (x >= 0)

    Returns:
        Total count of increasing or decreasing numbers below 10^x
    """
    if x == 0:
        return 1

    inc = math.comb(x + 9, 9)
    dec = math.comb(x + 10, 10) - x
    comm = 9 * x + 1

    return inc + dec - comm


if __name__ == "__main__":
    # Test cases
    test_cases = [
        (0, 1),
        (1, 10),
        (2, 100),
        (3, 475),
        (4, 1675),
        (5, 4954),
        (6, 12952),
    ]

    print("Testing total_inc_dec function:")
    print("-" * 50)
    for x, expected in test_cases:
        result = total_inc_dec(x)
        status = "✓" if result == expected else "✗"
        print(f"{status} x={x}: {result} (expected: {expected})")
