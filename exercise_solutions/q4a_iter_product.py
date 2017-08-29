#!/usr/bin/python3

def product(ip_iterable):
    op = 1
    for n in ip_iterable:
        op *= n
    return op

assert product([1, 4, 21]) == 84
assert product([-4, 2.3e12, 77.23, 982, 0b101]) == -3.48863356e+18
assert product((-3, 11, 2)) == -66
assert product({8, 300}) == 2400
assert product([234, 121, 23, 945, 0]) == 0
assert product(range(1, 6)) == 120

print('all tests passed')
