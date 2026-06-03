'''Test script for Goldbach's conjecture function'''
def is_prime(n):
    if n < 2:
        return False

    s = [True] * (n + 1)
    s[0] = s[1] = False

    for i in range(2, int(n**0.5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return s[n]



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

#IT IS PRETTY SLOW SO IT IS NOT RECOMMENDED TO TEST WITH LARGE NUMBERS