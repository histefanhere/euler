#!/usr/bin/env python3
"""Project Euler #2 - Even Fibonacci numbers (12/01/2021)"""

def solve():
    """Not a computationally difficult algorithm to implement in the slightest"""
    cur = 1
    prev = 1
    total = 0

    while cur < 4_000_000:
        if cur % 2 == 0:
            total += cur
        prev, cur = cur, prev + cur

    return total

if __name__ == "__main__":
    print(solve())
