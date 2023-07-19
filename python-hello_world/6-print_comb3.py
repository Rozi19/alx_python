#!/usr/bin/python
x = 0
while x < 10:
    y = x + 1
    while y < 10:
        if x != 8:
            print("{}{}, ".format(x, y), end = '')
        else:
            print("89")
        y += 1
    x += 1
