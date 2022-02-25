#!/usr/bin/env python3
"""Project Euler #14 - Longest Collatz sequence (14/08/2020)"""

def collatz(x):
    n = 0
    while x != 1:
        n += 1
        if x % 2 == 0:
            x = x >> 1
        else:
            x = 3 * x + 1
    return n

def solve():
    l, ll = 0, 0
    for i in range(1, 1_000_000):
        ln = collatz(i)
        if ln > ll:
            l, ll = i, ln

    return l

if __name__ == "__main__":
    print(solve())
