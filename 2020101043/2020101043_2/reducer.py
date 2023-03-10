#!/usr/bin/env python3
"""reducer.py"""

import sys

first_arr = []
sec_dict = {}
ans = 0
num_up = 0
newline = 0
# print("orey aazaamu")

for line in sys.stdin:
    line = line.strip()
    # print(line)
    # print(f"line: {line}")
    # parse the input
    word, count = line.split('\t', 1)
    
    if count[0] == '0':
        count = [ int(x) for x in count.split(' ') ]
        count.pop(0)
        first_arr = count

        for k, v in sec_dict.items():
            ans += first_arr[k] * v
            num_up += 1
    else:
        count = [ int(x) for x in count.split(' ') ]
        count.pop(0)
        if len(first_arr) == 0:
            sec_dict[count[1]] = count[0]
        else:
            ans += first_arr[count[1]] * count[0]
            num_up += 1
    
    if num_up == len(first_arr):
        print(str(ans) + ' ', end='')

        ans = 0
        num_up = 0
        first_arr = []
        sec_dict = {}

        newline += 1
        if newline % count[2] == 0:
            print()
        
        if newline == len(first_arr) * count[2]:
            break
        
