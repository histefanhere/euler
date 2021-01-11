#!/usr/bin/env python3
"""Project Euler #25 - 1000-digit Fibonacci number (10/01/2021)"""

import time

cur = 1
prev = 0
i = 1

threshold = 10 ** (1000 - 1)

while True:
    prev, cur = cur, prev + cur
    i += 1
    if cur >= threshold:
        break

print(i)

