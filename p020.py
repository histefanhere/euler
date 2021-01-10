#!/usr/bin/env python3
# 24/11/2020

import euler
euler.begin(20, "Factorial Digit Sum")

import math

num = str(math.factorial(100))

total = sum(int(x) for x in num)

euler.end(total)
    
