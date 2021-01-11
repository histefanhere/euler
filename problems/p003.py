#!/usr/bin/env python3
"""Project Euler #3 - Largest prime factor (14/08/2020)"""

def solve():
    n = 600851475143
    div = 2

    largest_factor = 0

    while True:
        if n % div == 0:
            largest_factor = n
            n = n / div
            if n == 1:
                return largest_factor
        else:
            div = div + 1

if __name__ == "__main__":
    print(solve())
