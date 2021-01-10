#!/usr/bin/env python3
# 10/01/2021

import euler
euler.begin(25, "1000-digit Fibonacci number")

import time


cur = 1
prev = 0
i = 1

threshold = 10 ** (1000 - 1)

start_time = time.time()


while True:
    prev, cur = cur, prev + cur
    i += 1
    if cur >= threshold:
        break

print(i)

end_time = time.time()

elapsed = end_time - start_time
euler.end("elapsed time", elapsed)
