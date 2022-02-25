#!/usr/bin/env python3
"""Project Euler #751 - Concatenation Coincidence (25/02/2022)"""

from decimal import Decimal, getcontext
from math import floor


N_MAX = 24
getcontext().prec = N_MAX + 1

def do_sequence(theta):
    b_n = theta
    sequence = "2."
    while len(sequence) < N_MAX + 2:
        new_bn = floor(b_n) * (b_n - floor(b_n) + 1)
        sequence += str(floor(new_bn))
        b_n = new_bn
    
    return sequence

def solve():
    n = Decimal('2')
    point = Decimal('1')

    # For each digit of the output...
    for i in range(N_MAX):
        point /= 10
        for x in range(10):
            # We try (sequencially) every 2.X value when i=1, 2.aX when i=2, 2.abX when i=3 etc.
            # And see which value of X matches the corresponding digits of the sequence
            trial_n = n + point * x
            sequence = do_sequence(trial_n)
            if str(trial_n) == sequence[0:(3 + i)]:
                n = trial_n
                break

    return n

if __name__ == "__main__":
    print(solve())
