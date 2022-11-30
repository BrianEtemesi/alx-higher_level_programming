#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 15 == 0):
            num = "FizzBuzz"
        elif (i % 5 == 0):
            num = "Buzz"
        elif (i % 3 == 0):
            num = "Fizz"
        else:
            num = i
        print("{} ".format(num), end='')

fizzbuzz()
print("")
