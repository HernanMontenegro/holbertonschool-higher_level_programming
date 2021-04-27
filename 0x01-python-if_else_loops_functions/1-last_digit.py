#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = 0
if number < 0:
    last_digit = -number % 10
    last_digit *= -1
else:
    last_digit = number % 10
print("The last digit of " + '{:d}'.format(number) + " is ", end='')
if last_digit > 5:
    print('{:d}'.format(last_digit) + " and is greater than 5")
elif last_digit == 0:
    print('{:d}'.format(last_digit) + " and is 0")
elif last_digit < 6 and last_digit != 0:
    print('{:d}'.format(last_digit) + " and is less than 6 and not 0")
