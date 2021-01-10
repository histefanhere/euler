#!/usr/bin/env python3
# 23/11/2020

import euler
euler.begin(16, "Power Digit Sum")

num_str = str(2 ** 1000)
total = sum(int(x) for x in num_str)

euler.end(total)
