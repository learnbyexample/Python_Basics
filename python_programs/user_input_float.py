#!/usr/bin/python3

usr_ip = input("Enter a floating point number: ")

# Need to explicitly convert input string to desired type
usr_num = float(usr_ip)
sqr_num = usr_num * usr_num

# Limit the number of digits after decimal points to 2
print("Square of entered number is: {0:.2f}".format(sqr_num))
