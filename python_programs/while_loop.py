#!/usr/bin/python3

# continuously ask user input till it is a positive integer
usr_string = 'not a number'
while not usr_string.isnumeric():
    usr_string = input("Enter a positive integer: ")
