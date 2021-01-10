#!/usr/bin/env python3
# 10/01/2021

import euler
euler.begin(24, "Lexicographic permutations")

digits = range(0, 10)
digits = list(str(x) for x in digits)

i = 1

def scan(pattern, remain):
    global i
    if len(remain) > 0:
        for digit in remain:
            scan(pattern + digit, list(filter(lambda x: x != digit, remain)))
    else:
        if i == 1_000_000:
            euler.end(pattern)

        i += 1

scan("", digits)
