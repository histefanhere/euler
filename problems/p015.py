#!/usr/bin/env python3
"""Project Euler #15 - Lattice paths (23/11/2020)"""

import math

# Not working
def calculate_slice(n, dimension):
    if dimension == 1:
        return n
    else:
        total = 0
        for i in range(1, n+1):
            total += calculate_slice(i, dimension-1)
        return total

# Not working
def calculate(n, dimension):
    total = 1

    for i in range(0, dimension):
        total = total * (n + i)

    return total / math.factorial(dimension)


# Working!
def calculate_grid_paths(size):
    # Took too long
    #return calculate_slice(size+1, size)

    # Simplified below
    #return calculate(size+1, size)

    return math.factorial(2 * size) / ( math.factorial(size) ) ** 2

def solve():
    return calculate_grid_paths(20)

if __name__ == "__main__":
    print(solve())

