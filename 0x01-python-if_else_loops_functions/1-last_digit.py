#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
reminder=number%10

if number >0 :
    # postive
    reminder = number % 10
    if reminder >5 and  number!=0:
        print(f"Last digit of {number} is {reminder} and is greater than 5")
    elif reminder <5 and  reminder!=0:
        print(f"Last digit of {number} is {reminder} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {reminder} and is 0 ")


elif number <0 :
    # negtive
    reminder = number % -10
    if reminder >5 and  number!=0:
        print(f"Last digit of {number} is {reminder} and is greater than 5")
    elif reminder <5 and  reminder!=0:
        print(f"Last digit of {number} is {reminder} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {reminder} and is 0 ")
