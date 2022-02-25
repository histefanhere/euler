#!/usr/bin/env python3
"""Project Euler #30 - Digit fifth powers (25/02/2022)"""

from itertools import combinations

# Largest possible numbers for x digits
# 4 * (9 ** 5) = 236196
# 5 * (9 ** 5) = 295245
# 6 * (9 ** 5) = 354294
# 7 * (9 ** 5) = 413343 (doesn't go to 7 digits!)

def solve():

    total = 0

    # Through experimentation, the numbers have to be 6 digits or less
    for i in range(2, 1_000_000):
        if sum(int(x) ** 5 for x in str(i)) == i:
            total += i

    return total

if __name__ == "__main__":
    print(solve())
