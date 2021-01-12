#!/usr/bin/env python3
"""Project Euler #56 - Powerful digit sum (12/01/2021)"""

def solve():
    """The easiest way to solve this problem is to brute-force it :P"""
    m = 0
    for a in range(1, 100):
        for b in range(1, 100):
            digit_sum = sum(int(x) for x in str(a ** b))
            m = max(m, digit_sum)

    return m

if __name__ == "__main__":
    print(solve())
