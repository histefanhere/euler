#!/usr/bin/env python3
"""Project Euler #12 - Highly divisible triangular number (07/03/2023)"""

from utility import primes_under

def solve():
    primes = list(primes_under(2 ** 16))

    n = 1
    while True:
        result = 1
        i = 0
        tri = n * (n + 1) // 2

        # Calculate how many prime divisors the triangular number has
        while tri != 1:
            # See how often primes[i] goes into n
            if tri % primes[i] == 0:
                count = 0
                while tri % primes[i] == 0:
                    count += 1
                    tri //= primes[i]
                result *= count + 1
            i += 1

        if result > 500:
            return n * (n + 1) // 2
        
        n = n + 1

if __name__ == "__main__":
    print(solve())
