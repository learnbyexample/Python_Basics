#!/usr/bin/python3

with open('f1.txt', 'r', encoding='ascii') as f:
    total = 0
    for line in f:
        num = int(line) if type(line) == int else float(line)
        #try:
        #    num = int(line)
        #except ValueError:
        #    num = float(line)
        total += num

    assert total == 10485.14

print('test passed')
