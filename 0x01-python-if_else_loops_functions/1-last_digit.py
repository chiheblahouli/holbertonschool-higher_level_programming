#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    p = abs(number) % 10
    p *= -1
else:
    p = number % 10
if p > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, p))
elif p > 5:
    print("Last digit of {:d} is {:d} and is 5".format(number, p))
elif p < 6 and p != 0:
    print("Last digit of {:d} is {:d} and is less than\
 6 and not 0".format(number, p))
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, p))
