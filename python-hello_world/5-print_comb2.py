#!/usr/bin/python3
for x in range(100):
    if x < 10:
        print("0{}, ".format(x), end ='')
    else:
        print("99\n" if x == 99 else "{}, ".format(x), end = '')
