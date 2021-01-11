#!/usr/bin/env python3
"""Project Euler #16 - Power digit sum (23/11/2020)"""

def solve():
    num_str = str(2 ** 1000)
    total = sum(int(x) for x in num_str)

    return total

if __name__ == "__main__":
    print(solve())

