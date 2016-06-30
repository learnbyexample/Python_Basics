#!/usr/bin/python3

import random

north = ['aloo tikki', 'baati', 'khichdi', 'makki roti', 'poha']
south = ['appam', 'bisibele bath', 'dosa', 'koottu', 'sevai']
west  = ['dhokla', 'khakhra', 'modak', 'shiro', 'vada pav']
east  = ['hando guri', 'litti', 'momo', 'rosgulla', 'shondesh']
zones = ['North', 'South', 'West', 'East']

choose_dish = [north, south, west, east]
rand_zone = random.randrange(4)
rand_dish = random.randrange(5)

zone = zones[rand_zone]
dish = choose_dish[rand_zone][rand_dish]
print("Would you like to have '{}' speciality '{}' today?".format(zone, dish))
