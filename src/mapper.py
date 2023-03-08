#!/usr/bin/env python3
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
i, row = 0, 0
m, n, p = -1, -1, -1
second = False
first_dict = {}

open("t2.txt", "w") # clear file

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    if i == 0:
        m, n = [ int(x) for x in line.split() ]
        i += 1
        row = 0
        continue 
    if m != -1 and n != -1 and i == m + 1:
        n, p = [ int(x) for x in line.split() ]
        for key, v in first_dict.items():
            for k in range(p):
                print('%s %s\t%s' % (str(key), str(k), "0 " + v) )   
                # with open ("t2.txt", "a+") as f:  
                    # f.write("first: ") 
                    # f.write('%s %s\t%s\n' % (str(key), str(k), "0 " + v) )
        i += 1
        row = 0
        second = True
        continue
    
    # with open ("t2.txt", "a") as f:
    #     f.write(line)

    if second == False:
        first_dict[row] = line 
    else:
        j = 0
        words = line.split()
        for word in words:
            # word = word.strip()
            for k in range(p):
                print('%s %s\t%s %s %s %s' % (str(k), str(j), "1", word, str(row), str(p)))
                # with open ("t2.txt", "a+") as f:
                    # f.write("second: ")
                    # f.write('%s %s\t%s\n' % (str(k), str(j), "1 " + word + ' ' + str(row) + ' ' + str(p)))
            j += 1

    i += 1
    row += 1

    if i > m + n + 1:
        break