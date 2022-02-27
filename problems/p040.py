#!/usr/bin/env python3
"""Project Euler #40 - Champernowne's constant (27/02/2022)"""

def solve():
    i = 0
    target = 1
    total = 1
    x = 1
    while target <= 1_000_000:
        i += len(str(x))
        if i >= target:
            total = total * int(str(x)[target - i - 1])
            target = target * 10
        x += 1
    
    return total

if __name__ == "__main__":
    print(solve())
