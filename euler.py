#!/usr/bin/env python3

import humanize
import datetime as dt

class Euler:
    def start(self, number, title):
        self.number = number
        self.title = title

        # TODO: Guess the project number from the main filename?

        print(f"PROJECT #{number}: {title}")

        # Start timing *now*, after the inital print statement
        self.start_time = dt.datetime.now()

# The reason this is here is so both the `begin` and `end` functions have access to the start time and such
# And the reason they're all spread out instead of being methods of a class is so that this module uses minimal
# characters in every project euler script
euler = Euler()

def begin(number, title):
    euler.start(number, title)

def end(*results):
    # Calculate the time it took for the program to run
    end_time = dt.datetime.now()
    delta = end_time - euler.start_time

    # TODO: This doesn't print very well small intervals

    print("\nDone!")
    print("Time elapsed:", humanize.precisedelta(delta))
    print("Result:", *results)

    # Since this is the last thing that will run in *all* the euler scripts, we can kill the program now.
    exit()

# TODO: If this module is executed, maybe list out how many euler projects have been done till now?
# - Which is the next in order to do
