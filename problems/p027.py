#!/usr/bin/env python3
"""Project Euler #27 - Quadratic primes (26/02/2022)"""

import itertools
from utility import is_prime, primes_under

def solve():
    max_consecutive_primes, max_a, max_b = 0, 0, 0

    # for a in range(-1000, 1000):
    #     for b in primes_under(1000):
    for a, b in itertools.product(range(-999, 1000, 2), primes_under(1000)):
            n = 0
            while True:
                if is_prime(n ** 2 + a * n + b):
                    n += 1
                else:
                    break

            if n > max_consecutive_primes:
                max_consecutive_primes, max_a, max_b = n, a, b
            
    return max_a * max_b

if __name__ == "__main__":
    print(solve())
