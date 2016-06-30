#!/usr/bin/python3

usr_ip = input("Enter an integer number: ")

# Need to explicitly convert input string to desired type
usr_num = int(usr_ip)
sqr_num = usr_num * usr_num

print("Square of entered number is: {}".format(sqr_num))
