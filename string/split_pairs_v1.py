"""
split_pairs_v1.py - Version 1

Inline description:
This module implements a solution that splits a string into pairs of two
characters. If the input string has an odd length the final pair is padded
with an underscore '_'. This is the first (unchanged) version taken from
an initial solution snapshot.

Behavior notes:
- Empty string -> []
- Single character -> [char + '_']
- Even length strings -> list of two-character substrings
- Odd length strings -> same as even but last element padded with '_'

This file intentionally preserves the original control-flow style.
"""

def solution(s):
    res = []
    lis = list(s)
    if len(s) % 2 == 0:
        i = 0
        while i < len(s) - 1:
            res.append(''.join([lis[i], lis[i+1]]))
            i += 2
        return res
    elif len(s) == 1:
        return [s + '_']
    else:
        i = 0
        while i < len(s) - 1:
            res.append(''.join([lis[i], lis[i+1]]))
            i += 2
        res.append(lis[-1] + '_')
        return res


if __name__ == "__main__":
    # Basic test cases for version 1
    tests = ["", "a", "ab", "abc", "abcd", "abcde"]
    print("split_pairs_v1 tests:")
    for t in tests:
        print(f"input={t!r} -> {solution(t)}")
