#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = str(number)
last_digit = int(num_str[-1])
-last_digit if (number < 0) else last_digit
if last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_digit))
elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_digit))
