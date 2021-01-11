#!/usr/bin/env python3
"""Project Euler #20 - Factorial digit sum (24/11/2020)"""

import math

num = str(math.factorial(100))

total = sum(int(x) for x in num)

print(total)
   
