#!/usr/bin/env python3
"""Project Euler #45 - Triangular, pentagonal, and hexagonal (27/02/2022)"""

def tria(x):
    return x * (x + 1) >> 1

def penta(x):
    return x * (3 * x - 1) >> 1

def hexa(x):
    return x * (2 * x - 1)

def solve():
    t, p, h = 285, 165, 143

    while True:
        h += 1
        value = hexa(h)

        # increment penta
        while True:
            p += 1
            if penta(p) > value:
                # We've overshot penta!
                p -= 1
                break
            elif penta(p) == value:
                # tria and penta match!
                while True:
                    t += 1
                    if tria(t) == value:
                        return value

if __name__ == "__main__":
    print(solve())
