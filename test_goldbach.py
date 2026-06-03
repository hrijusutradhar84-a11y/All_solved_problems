'''Test script for Goldbach's conjecture function'''
from math.is_prime import is_prime




def goldbach(even_number):
    res = []
    for i in range(2, even_number // 2 + 1):
        j = even_number - i
        if is_prime(i) and is_prime(j):
            res.append([i, j])
    return res

# Test cases
print("Testing goldbach function:")
print(f"goldbach(6) = {goldbach(6)}")
print(f"goldbach(8) = {goldbach(8)}")
print(f"goldbach(10) = {goldbach(10)}")
print(f"goldbach(18) = {goldbach(18)}")
print(f"goldbach(34) = {goldbach(34)}")
print(f"goldbach(100) = {goldbach(100)}")
