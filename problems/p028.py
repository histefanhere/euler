#!/usr/bin/env python3
"""Project Euler #28 - Number spiral diagonals (11/01/2021)"""

# We have to subtract 3 because the formula is the sum of the formulas for all the diagonals
# Meaning the inital `1` is counted 4 times instead of just once
def solve():
    func = lambda x: 16 * (x ** 2) - 28 * x + 16

    total = 0
    # In my calculation I took a 1x1 square to be n=1, 3x3 to be n=2, 5x5 to be n=3 and so on.
    # Hence the ugly conversion code from the number "1001" to what my function takes
    # (and +1 to be inclusive)
    for i in range(1, (1001+1)//2+1):
        total += func(i)

    return total - 3

if __name__ == "__main__":
    print(solve())
