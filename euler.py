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

def time_to_str(delta):
    """Converts a seconds integer to a human-readable string"""
    if delta > 1:
        # Program took more than one second
        return f"{delta:.2f}s"
    elif delta > 1e-3:
        # More than a millisecond (1/1000 of a second)
        return f"{delta*1e3:.2f}ms"
    elif delta > 1e-6:
        # More than a microsecond (1/1_000_000 of a second)
        return f"{delta*1e6:.1f}µs"
    else:
        # Less than a microsecond, so in the nanoseconds or even less - bruuuh
        return f"{delta*1e9:.2f}ns"

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
solve_time = 0
input_time = 0
if hasattr(module, 'get_input'):
    start_time = timer()
    input = module.get_input()
    input_time = timer() - start_time

    start_time = timer()
    output = module.solve(input)
    solve_time = timer() - start_time
else:
    start_time = timer()
    output = module.solve()
    solve_time = timer() - start_time

time_string = f" ({time_to_str(input_time)} to read input)" if input_time > 0 else ''

print("\nDone!")
print(f"Time elapsed: {time_to_str(solve_time + input_time)}{time_string}")
print("Result:", output)
