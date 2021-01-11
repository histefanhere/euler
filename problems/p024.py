#!/usr/bin/env python3
"""Project Euler #24 - Lexicographic permutations (10/01/2021)"""

digits = range(0, 10)
digits = list(str(x) for x in digits)

i = 1
found = False

def scan(pattern, remain):
    global found
    global i
    if len(remain) > 0:
        for digit in remain:
            scan(pattern + digit, list(filter(lambda x: x != digit, remain)))
            if found:
                break
    else:
        if i == 1_000_000:
            print(pattern)
            found = True

        i += 1

scan("", digits)
