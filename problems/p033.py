#!/usr/bin/env python3
"""Project Euler #33 - Digit cancelling fractions (27/02/2022)"""

from math import gcd

def solve():

    a_total = 1
    b_total = 1
    
    for a in range(10, 100):
        for b in range(a + 1, 100):
            # If we remove some digit from a/b to get a_new/b_new, is a * b_new = b * a_new?
            for digit in str(a):
                if digit != "0" and digit in str(b):
                    a_new = int(str(a).replace(digit, '', 1))
                    b_new = int(str(b).replace(digit, '', 1))

                    if a * b_new == b * a_new:
                        a_total = a_total * a
                        b_total = b_total * b

    while True:
        divisor = gcd(a_total, b_total)
        if divisor == 1:
            break
        else:
            a_total, b_total = a_total // divisor, b_total // divisor

    return b_total

if __name__ == "__main__":
    print(solve())
