#!/usr/bin/python3
for x in range(100):
    if x < 10:
        print("0{}, ".format(x), end ='')
    else:
        if x > 9 and x < 99:
            print("{}, ".format(x), end = '')
        else:
            print("{}".format(x))