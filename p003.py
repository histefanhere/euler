#!/usr/bin/env python3
# 14/08/2020

import euler
euler.begin(3, "Largest Prime Factor")

n = 600851475143
div = 2

largest_factor = 0

while True:
    if n % div == 0:
        largest_factor = n
        n = n / div
        if n == 1:
            euler.end(largest_factor)
    else:
        div = div + 1

