#!/usr/bin/env python3
"""Project Euler #17 - Number letter counts (23/11/2020)"""

import math

def num_to_str(n):
    # Only designed to work with numbers from 1 to 1000 (inclusive)

    ones = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",

            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen"
    }
    tens = {
            2: "twenty",
            3: "thirty",
            4: "forty",
            5: "fifty",
            6: "sixty",
            7: "seventy",
            8: "eighty",
            9: "ninety"
    }

    output = []

    if n >= 1000:
        digit = math.floor(n / 1000) % 10
        output.append(f"{ones[digit]} thousand")

    hundreds_digit = math.floor(n / 100) % 10
    if hundreds_digit > 0:
        output.append(f"{ones[hundreds_digit]} hundred")

    tens_digit = math.floor(n / 10) % 10
    
    ones_digit = math.floor(n / 1) % 10

    if (ones_digit != 0 or tens_digit != 0) and len(output) != 0:
        output.append("and")

    if tens_digit == 0:
        if ones_digit != 0:
            output.append(ones[ones_digit])

    elif tens_digit == 1:
        output.append(ones[tens_digit * 10 + ones_digit])

    else:
        # tens is 2 - 9
        output.append(tens[tens_digit])


        if ones_digit != 0:
            output.append(ones[ones_digit])

    return " ".join(output)

letters = 0
for i in range(1, 1001):
    letters += len(list(char for char in num_to_str(i) if char != " "))

print(letters)
