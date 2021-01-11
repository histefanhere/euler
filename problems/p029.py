#!/usr/bin/env python3
"""Project Euler #29 - Distinct Powers (11/01/2021)"""

def solve():
    MIN = 2
    MAX = 100

    nums = []

    for i in range(MIN, MAX+1):
        for j in range(MIN, MAX+1):
            power = i ** j
            if power not in nums:
                nums.append(power)

    return len(nums)


if __name__ == "__main__":
    print(solve())
