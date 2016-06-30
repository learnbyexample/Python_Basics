#!/usr/bin/python3

import random

while True:
    # as with range() function, 500 is not inclusive
    random_int = random.randrange(500)
    if random_int % 4 == 0 and random_int % 6 == 0:
        break
print("Random number divisible by 4 and 6: {}".format(random_int))
