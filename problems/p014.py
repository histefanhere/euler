#!/usr/bin/env python3
"""Project Euler #14 - Longest Collatz sequence (14/08/2020)"""

def iterate(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

longest_chain_number = 0
longest_chain_length = 0

ignore = []

for i in range(1_000_000, 2, -1):
    if i in ignore:
        continue
    print(i)

    chain_length = 1
    n = i

    while n != 1:
        ignore.append(n)
        n = iterate(n)
        if n in ignore:
            break   
        chain_length += 1

    if chain_length > longest_chain_length:
        longest_chain_number = i
        longest_chain_length = chain_length

print(longest_chain_number, longest_chain_length)
