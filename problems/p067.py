#!/usr/bin/env python3
"""Project Euler #67 - Maximum path sum II (23/11/2020)"""

def get_input():
    with open('resources/p067_triangle.txt', 'r') as file:
        return [[int(x) for x in line.split(' ')] for line in file.read().splitlines()]

def solve(nums):
    # goes from second to last row to first row
    for i in range(len(nums)-2, -1, -1):
        for j in range(i+1):
            # We should consider nums[i+1][j] and nums[i+1][j+1]
            nums[i][j] += max(nums[i+1][j], nums[i+1][j+1])

    return nums[0][0]

if __name__ == "__main__":
    print(solve(get_input()))
