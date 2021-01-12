# euler

This is a repository of all my [Project Euler](https://projecteuler.net) problem solution scripts and a suite of tools made to make solving problems easier.

**WARNING: I _highly_ recommend to delete all my problem solutions in `problems`.** The "Aha!" moment when you solve a problem is priceless, and glimpsing past a solution will spoil that moment from you forever. The _only_ reason the problems are even uploaded to the repo in the first place is as a record-keeper for me.

That being said, once you've already solved a problem seeing how others have done it might give you better insight into the maths and algorithms at play, so here the decision is yours.

## What is Project Euler?

From the [Project Euler](https://projecteuler.net) website,

> Project Euler is a series of challenging mathematical/computer programming problems that will require more than just mathematical insights to solve. Although mathematics will help you arrive at elegant and efficient methods, the use of a computer and programming skills will be required to solve most problems.
> 
> The motivation for starting Project Euler, and its continuation, is to provide a platform for the inquiring mind to delve into unfamiliar areas and learn new concepts in a fun and recreational context.

## Usage

`generate.py` is used to generate template scripts when you start coding a new problem - all it needs to be supplied with is the problem ID. With these it generates a file like this one:

```
euler/problems$ cat p001.py
#!/usr/bin/env python3
"""Project Euler #1 - Multiples of 3 and 5 (11/01/2021)"""

def solve():
    # Your code here!
    pass

if __name__ == "__main__":
    print(solve())
```

these files can be ran stand-alone in several ways:
```bash
# using the template, scripts can be executed directly
euler/problems$ ./p001.py
42000
# Or specify python3 if that's your jazz.
euler/problems$ python3 p001.py
42000
```

Or using the `euler` tool by simply passing it the problem ID, which will also automatically time the script:
```
euler$ ./euler 1
Project Euler #1 - Multiples of 3 and 5 (11/01/2021)

Done!
Time elapsed: 3.56 seconds
Result: 42000
```

## Contributing

If you want to contribue - thanks! Issues and pull requests of all shapes and sizes are welcomed with open arms here

