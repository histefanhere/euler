#!/usr/bin/env python3
"""Project Euler #48 - Self powers (26/02/2022)"""

def solve():
    digits = 0

    for x in range(1, 1000 + 1):
        digits = (digits + x ** x) % 10_000_000_000

    return digits

if __name__ == "__main__":
    print(solve())
