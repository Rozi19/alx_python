#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        a = int(a)
        b = int(b)
        div = a / b
    except ZeroDivisionError:
         print("Inside result: {}".format(None))
         print("{} / {} = {}".format(a, b, None))
    finally:
        print("Inside result: {}".format(div))
        return div
