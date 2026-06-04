"""Sum of Digits
Problem: Calculate the sum of all digits in a number
Example: sum_of_digits(123) = 1 + 2 + 3 = 6
"""

def sum_of_digits(n):
    """
    Returns the sum of all digits in the given number.

    Args:
        n: A non-negative integer

    Returns:
        The sum of all digits
    """
    total = 0
    for digit in str(n):
        total += int(digit)
    return total


if __name__ == "__main__":
    # Test cases
    print(f"sum_of_digits(123) = {sum_of_digits(123)}")  # Expected: 6
    print(f"sum_of_digits(9875) = {sum_of_digits(9875)}")  # Expected: 29
    print(f"sum_of_digits(0) = {sum_of_digits(0)}")  # Expected: 0
