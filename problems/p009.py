#!/usr/bin/env python3
"""Project Euler #9 - Special Pythagorean triplet (25/02/2022)"""

def solve():
    # since a has to be the smallest of the three, it cannot exceed 1/3 of 1000 (otherwise one other would have to be less)
    for a in range(333 + 1):

        # b has to be less than 1000 - a in order for c to be larger than b
        for b in range(a + 1, (1000 - a) >> 1):
            
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
    
    return 0

if __name__ == "__main__":
    print(solve())
