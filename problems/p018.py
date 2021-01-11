#!/usr/bin/env python3
"""Project Euler #18 - Maximum path sum I (23/11/2020)"""

import util

filename = util.get_resource_path("p018_triangle.txt")

nums = []

with open(filename, "r") as file:
    for line in file.readlines():
        line_nums = list(int(x) for x in line.split())
        nums.append(line_nums)

rows = len(nums)


for i in range(rows-2, -1, -1):
    # goes from second to last row to first row

    for j in range(i+1):
        # We should consider nums[i+1][j] and nums[i+1][j+1]

        nums[i][j] += max(nums[i+1][j], nums[i+1][j+1])

print(nums[0][0])
