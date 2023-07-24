#!/usr/bin/python3
import sys

def main():
    x = len(sys.argv)
    if x == 0:
        print("0 arguments.")
    elif x == 1:
        print("{} argument:".format(x))
        for i in range(1, x):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments:".format(x))
        for i in range(1, x):
            print("{}: {}".format(i, sys.argv[i]))
if __name__ == "__main__":
    main()
