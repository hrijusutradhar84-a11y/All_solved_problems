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
