#!/usr/bin/env python3
"""Project Euler #1 - Multiples of 3 and 5 (12/01/2021)"""

def solve():
    """one liner :)"""
    return sum(x for x in range(1000) if (x % 5 == 0) or (x % 3 == 0))

if __name__ == "__main__":
    print(solve())
