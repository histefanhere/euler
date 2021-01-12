#!/usr/bin/env python3
"""Generate a new templated script for a Project Euler problem

Given the ID of a Project Euler problem, a new executable script will be
generated in `problems` for the problem according to the `template` variable below
"""

import datetime as dt
import os
import stat
import requests
from bs4 import BeautifulSoup
import argparse

PROBLEMS_DIR = "problems"

template = '''\
#!/usr/bin/env python3
"""Project Euler #{id} - {title} ({date})"""

def solve():
    # Your code here!
    pass

if __name__ == "__main__":
    print(solve())
'''

parser = argparse.ArgumentParser(description="Generate template Project Euler scripts")
parser.add_argument('id', nargs='?', type=int, help="project ID to be generated")
args = parser.parse_args()

if args.id is not None:
    # ID was given as an argument
    project_id = args.id
else:
    print("This script will generate a starting script for you to solve your project euler problem in.")

    try:
        project_id = int(input("What is the ID number of the problem? "))
    except ValueError:
        print("That isn't an integer!")
        exit()

filename = PROBLEMS_DIR + '/p{:0>3}.py'.format(project_id)

# Check if the file already exists - if it does, chances are it has some code in it.
# And you don't want to be erasing code!
if os.path.exists(filename):
    print("There is a file that already exists under that name!")
    exit()

# Fetch the problem name from the website
text = requests.get('https://projecteuler.net/problem={}'.format(project_id)).text
project_title = BeautifulSoup(text, 'html.parser').find('h2').string
print("Problem #{} - {}".format(project_id, project_title))

date = dt.datetime.now().strftime("%d/%m/%Y")

content = template.format(id=project_id, title=project_title, date=date)

# Create the file with the formatted template content
with open(filename, 'w+') as file:
    file.write(content)

# Once we've made the file, we want to make it executable (because, well, why not :))
# https://stackoverflow.com/questions/12791997
st = os.stat(filename)
os.chmod(filename, st.st_mode | stat.S_IEXEC)

print("Done! Check out {}".format(filename))
