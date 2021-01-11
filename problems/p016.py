#!/usr/bin/env python3
"""Project Euler #16 - Power digit sum (23/11/2020)"""

num_str = str(2 ** 1000)
total = sum(int(x) for x in num_str)

print(total)
