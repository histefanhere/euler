#!/usr/bin/env python3
"""Project Euler #67 - Maximum path sum II (23/11/2020)"""

import util
filename = util.get_resource_path('p067_triangle.txt')

nums = []

with open(filename, "r") as file:
    for line in file.readlines():
        line_nums = list(int(x) for x in line.split())
        nums.append(line_nums)

rows = len(nums)

def solve():
    for i in range(rows-2, -1, -1):
        # goes from second to last row to first row

        for j in range(i+1):
            # We should consider nums[i+1][j] and nums[i+1][j+1]

            nums[i][j] += max(nums[i+1][j], nums[i+1][j+1])

    return nums[0][0]

if __name__ == "__main__":
    print(solve())

