#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Random number is {}".format(number))
a = str(number)
b = int(a[-1])
if number < 0:
    b = b * -1
print("Last digit of {} is {} ".format(number, b), end="")
if b > 5:
    print("and is greater than 5")
elif b == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
