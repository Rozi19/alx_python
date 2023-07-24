#!/usr/bin/python3
import sys

x = len(sys.argv)
if x == '':
    print("0 arguments.")
elif (x) == 1:
    print("{} argument:".format(x))
    for i in range(1, x):
        print("{}: {}".formt(i, sys.argv[i]))
else:
    print("{} arguments:".format(x))
    for i in range(1, x):
        print("{}: {}".format(i, sys.argv[i]))
