#!/usr/bin/env python3
# 24/11/2020

import euler
euler.begin(19, "Counting Sundays")

# 1 Jan 1900 was monday
# thirty days in sep, april, june, nov
# all rest have 31
# february twenty eight and leap 29
# leap: % 4 == 0 and (not % 100 == 0 or % 400 == 0)

base_periods = {
        1: 31,
        2: [28, 29],
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
}

def get_days(month, year):
    # Get the amount of days in the month given the year.
    # The year is needed because february changes

    if month != 2:
        return base_periods[month]
    else:
        if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
            # If it's a leap year...
            return base_periods[2][1]
        else:
            return base_periods[2][0]

# week goes from monday to sunday, 0 to 6.
# sunday == 6

year = 1900
month = 1
dow = 0

sundays_on_first_of_month = 0

while True:
    # iterate
    days_in_month = get_days(month, year)

    dow = (dow + days_in_month) % 7

    month = month + 1

    if month == 13:
        month = 1
        year += 1

    if year >= 1901 and year <= 2000:
        if dow == 6:
            sundays_on_first_of_month += 1

    if year > 2000:
        break

euler.end(sundays_on_first_of_month)

