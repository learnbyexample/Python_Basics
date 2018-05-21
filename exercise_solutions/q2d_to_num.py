#!/usr/bin/python3

def num(ip):
    if type(ip) in (int, float):
        return ip
    elif type(ip) != str:
        raise TypeError('not a valid input')

    try:
        return int(ip)
    except ValueError:
        try:
            return float(ip)
        except ValueError:
            raise ValueError('could not convert string to int or float')

assert num(3) == 3
assert num(0x1f) == 31
assert num(0b101) == 5
assert num(0o10) == 8
assert num(3.32) == 3.32
assert num('123') == 123
assert num('-78') == -78
assert num(" 42  \n ") == 42
assert num('3.14') == 3.14
assert num('3.982e5') == 398200.0
s = '56'
assert num(s) + 44 == 100
s = '8' * 10
assert num(s) == 8888888888

assert type(num('42')) == int
assert type(num('1.23')) == float

try:
    num('foo')
except ValueError as e:
    assert str(e) == 'could not convert string to int or float'

try:
    num(['1', '2.3'])
except TypeError as e:
    assert str(e) == 'not a valid input'

print('all tests passed')
