#!/usr/bin/env python3
"""Run and time a project euler script from the given ID"""

import argparse
import importlib
import glob
import os
from timeit import default_timer as timer

PROBLEMS_DIR = "problems"

def id_to_module(project_id):
    """Given a ID, convert it to a module"""
    return 'p{:0>3}'.format(project_id)


# Parse the ID from the command line via `argparse`
parser = argparse.ArgumentParser(description="Run a Project Euler project")
parser.add_argument('id', nargs='?', type=int, help='project ID to be executed')
args = parser.parse_args()


if args.id is None:
    # User ran the euler script with no arguments, meaning
    # They wish to simply see stats

    # Find all the problem script files
    files = glob.glob(PROBLEMS_DIR + '/p[0-9][0-9][0-9].py')
    total_files = len(files)

    # Algorithm for finding the first problem without a script
    i = 0
    while True:
        i += 1
        if os.path.join('problems', id_to_module(i) + '.py') not in files:
            break

    print("You've created scripts for {} Project Euler problem{}".format(
        total_files,
        's' if total_files > 1 else ''
    ))

    print("The next problem in order you have to solve is Problem #{}".format(i))

    exit()


modulename = PROBLEMS_DIR + '.' + id_to_module(args.id)

try:
    module = importlib.import_module(modulename)
except ModuleNotFoundError:
    print("That problem script doesn't exist!")
    exit()

# Show the title of the script, generated via `generate.py`
print(module.__doc__)

# Make sure we're only timing the solving of the problem


start_time = timer()
output = module.solve()
end_time = timer()

delta = end_time - start_time

print("\nDone!")
if delta > 1:
    # Program took more than one second
    print(f"Time elapsed: {delta:.2f}s")
elif delta > 1e-3:
    # More than a millisecond (1/1000 of a second)
    print(f"Time elapsed: {delta*1e3:.2f}ms")
elif delta > 1e-6:
    # More than a microsecond (1/1_000_000 of a second)
    print(f"Time elapsed: {delta*1e6:.1f}µs")
else:
    # Less than a microsecond, so in the nanoseconds or even less - bruuuh
    print(f"Time elapsed: {delta*1e9:.2f}ns")
print("Result:", output)

