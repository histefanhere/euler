#!/usr/bin/env python3
"""Project Euler #22 - Names scores (24/11/2020)"""

def get_input():
    with open("resources/p022_names.txt", "r") as file:
        return file.read().replace('"', '').split(',')

def solve(names):
    names.sort()

    total_score = 0
    for i, name in enumerate(names):
        total_score += (i + 1) * sum(ord(letter) - ord('A') + 1 for letter in name)

    return total_score

if __name__ == "__main__":
    print(solve(get_input()))
