#!/usr/bin/python3

while True:
    try:
        usr_num = int(input("Enter an integer number: "))
        break
    except ValueError:
        print("Not an integer, try again")

print("Square of entered number is: {}".format(usr_num * usr_num))
