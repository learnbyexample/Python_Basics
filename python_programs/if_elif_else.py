#!/usr/bin/python3

num = 45

# only if
if num > 25:
    print("Hurray! {} is greater than 25".format(num))

# if-else
if num % 2 == 0:
    print("{} is an even number".format(num))
else:
    print("{} is an odd number".format(num))

# if-elif-else
# any number of elif can be used
if num < 0:
    print("{} is a negative number".format(num))
elif num > 0:
    print("{} is a positive number".format(num))
else:
    print("{} is neither postive nor a negative number".format(num))
