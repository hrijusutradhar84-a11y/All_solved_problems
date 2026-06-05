"""
split_pairs_v2.py - Version 2

Inline description:
Refactored version that uses slicing and a single loop to build pairs. Handles
both even and odd length inputs and pads the last character with '_' when
necessary. Slightly cleaner control flow than version 1.
"""

def solution(s):
    res = []
    lis = list(s)
    i = 0
    j = 0
    if len(s) % 2 == 0:
        while i < len(s):
            res.append(''.join(lis[i : i+2]))
            i += 2
        return res
    elif len(s) == 1 or len(s) % 2 != 0:
        while j < (len(s) - 1):
            res.append(''.join(lis[j : j + 2]))
            j += 2
        res.append(''.join((lis[-1], '_')))
        return res


if __name__ == "__main__":
    # Basic test cases for version 2
    tests = ["", "a", "ab", "abc", "abcd", "abcde"]
    print("split_pairs_v2 tests:")
    for t in tests:
        print(f"input={t!r} -> {solution(t)}")
