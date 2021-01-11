#!/usr/bin/env python3
"""Project Euler #24 - Lexicographic permutations (10/01/2021)"""

i = 1

def solve():
    digits = range(0, 10)
    digits = list(str(x) for x in digits)


    def scan(pattern, remain):
        global i
        if len(remain) > 0:
            for digit in remain:
                return_val = scan(pattern + digit, list(filter(lambda x: x != digit, remain)))
                if return_val:
                    return return_val
        else:
            if i == 1_000_000:
                return pattern
            #i += 1
            i = i + 1

    return scan("", digits)

if __name__ == "__main__":
    print(solve())

