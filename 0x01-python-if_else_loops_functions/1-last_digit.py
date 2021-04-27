#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = 0
result = ""
if number < 0:
    last_digit = -number % 10
else:
    last_digit = number % 10
result = "The last digit of " + str(number) + " is " + str(last_digit) + " "
if last_digit > 5:
    result += "and is greater than 5"
elif last_digit == 0:
    result += "and is 0"
elif last_digit < 6 and last_digit != 0:
    result += "and is less than 6 and not 0"
print(result)
