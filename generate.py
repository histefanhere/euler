#!/usr/bin/env python3
"""Generate a new templated script for a Project Euler problem

Given the ID of a Project Euler problem and it's title, a new executable script will be
generated in `problems` for the problem according to the `template` variable below
"""

import datetime as dt
import os
import stat

template = '''\
#!/usr/bin/env python3
"""Project Euler #{id} - {title} ({date})"""

def solve():
    # Your code here!
    pass

if __name__ == "__main__":
    print(solve())
'''

print("This script will generate a starting script for you to solve your project euler problem in.")

try:
    project_id = int(input("What is the ID number of the problem? "))
except ValueError:
    print("That isn't an integer!")
    exit()

title = input("What's the title of the problem? ")

date = dt.datetime.now().strftime("%d/%m/%Y")

content = template.format(id=project_id, title=title, date=date)
filename = 'problems/p{:0>3}.py'.format(project_id)

# Check if the file already exists - if it does, chances are it has some code in it.
# And you don't want to be erasing code!
if os.path.exists(filename):
    print("There's a file that already exists under that name!")
    exit()

# Create the file with the formatted template content
with open(filename, 'w+') as file:
    file.write(content)

# Once we've made the file, we want to make it executable (because, well, why not :))
# https://stackoverflow.com/questions/12791997
st = os.stat(filename)
os.chmod(filename, st.st_mode | stat.S_IEXEC)

print("Done! Check out {}".format(filename))
