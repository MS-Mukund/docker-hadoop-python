#!/usr/bin/env python3
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
i, row = 0, 0
m, n, p = -1, -1, -1
second = False
first_dict = {}

# open("t2.txt", "w") # clear file

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    print(line)