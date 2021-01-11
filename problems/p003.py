#!/usr/bin/env python3
"""Project Euler #3 - Largest prime factor (14/08/2020)"""

n = 600851475143
div = 2

largest_factor = 0

while True:
    if n % div == 0:
        largest_factor = n
        n = n / div
        if n == 1:
            print(largest_factor)
            break
    else:
        div = div + 1

