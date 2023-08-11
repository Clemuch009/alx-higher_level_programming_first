#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_num = number

if number >= 0:
    if number == 0 or number % 10 == 0:
        print("Last digit of {:d} is 0 and is 0".format(number))
    elif number % 10 > 5:
        print("Last digit of {:d} is {:d} and is greater than 5".format
              (number, number % 10))
    else:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0".format
              (number, number % 10))

if number < 0:
    abs_num = number * -1
    print("Last digit of -{:d} is -{:d} and is less than 6 and not 0".format
          (abs_num, abs_num % 10))
