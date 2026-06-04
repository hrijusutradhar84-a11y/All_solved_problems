"""
Prime Number Utilities

Problem: Check if a number is prime, generate prime numbers, and find prime factors.

Time Complexity: O(sqrt(n)) for is_prime, O(n log log n) for sieve
Space Complexity: O(1) for is_prime, O(n) for sieve

Example:
    >>> is_prime(17)
    True
    >>> sieve_of_eratosthenes(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> prime_factors(60)
    [2, 2, 3, 5]
"""

def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): Number to check
    
    Returns:
        bool: True if prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def sieve_of_eratosthenes(n):
    """
    Generate all primes up to n using Sieve of Eratosthenes.
    
    Args:
        n (int): Upper limit
    
    Returns:
        list: All prime numbers up to n
    """
    if n < 2:
        return []
    
    is_prime_arr = [True] * (n + 1)
    is_prime_arr[0] = is_prime_arr[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime_arr[i]:
            for j in range(i*i, n + 1, i):
                is_prime_arr[j] = False
    
    return [i for i in range(2, n + 1) if is_prime_arr[i]]


def prime_factors(n):
    """
    Find prime factors of a number.
    
    Args:
        n (int): Number to factorize
    
    Returns:
        list: Prime factors
    """
    factors = []
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    
    if n > 1:
        factors.append(n)
    
    return factors


def count_primes(n):
    """
    Count number of primes less than n.
    
    Args:
        n (int): Upper limit
    
    Returns:
        int: Count of primes
    """
    return len(sieve_of_eratosthenes(n - 1))


if __name__ == "__main__":
    print("Test 1 (is_prime):", is_prime(17))       # True
    print("Test 2 (is_prime):", is_prime(20))       # False
    print("Test 3 (sieve):", sieve_of_eratosthenes(30))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    print("Test 4 (factors):", prime_factors(60))   # [2, 2, 3, 5]
    print("Test 5 (count):", count_primes(30))      # 9
