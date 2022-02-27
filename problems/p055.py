#!/usr/bin/env python3
"""Project Euler #55 - Lychrel numbers (28/02/2022)"""

def solve():
    total = 0
    for x in range(1, 10_000):
        run_x = x
        for _ in range(50):
            run_x += int(str(run_x)[::-1])
            if str(run_x) == str(run_x)[::-1]:
                break
        else:
            total += 1

    return total

if __name__ == "__main__":
    print(solve())
