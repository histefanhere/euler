#!/usr/bin/env python3
"""Project Euler #36 - Double-base palindromes (28/02/2022)"""

def solve():
    
    total = 0

    for i in range(1, 1_000_000):

        decimal = str(i)
        if decimal == decimal[::-1]:

            binary = format(i, 'b')
            if binary == binary[::-1]:
                total += i

    return total

if __name__ == "__main__":
    print(solve())
