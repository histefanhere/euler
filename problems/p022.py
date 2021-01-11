#!/usr/bin/env python3
"""Project Euler #22 - Names scores (24/11/2020)"""

import util

names = []

with open(util.get_resource_path("p022_names.txt"), "r") as file:
    raw_names = file.read().split(",")

    for name in raw_names:
        names.append(name.strip("\""))

names.sort()   

def solve():
    def get_letter_score(letter):
        return ord(letter) - ord('A') + 1

    total_scores = 0

    for i, name in enumerate(names):
        score = (i + 1) * sum(get_letter_score(letter) for letter in name)

        total_scores += score
    
if __name__ == "__main__":
    print(solve())

