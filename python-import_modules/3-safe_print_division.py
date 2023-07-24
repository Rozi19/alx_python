#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        a = int(a)
        b = int(b)
        div = a / b
    except ZeroDivisionError:
         pass
    finally:
        if b > 0:
            print("Inside result: {}".format(div))
            return div
        else:
            print("Inside result: {}".format(None))
