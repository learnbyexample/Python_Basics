#!/usr/bin/python3

import re

with open('f2.txt', 'r', encoding='ascii') as f:
    total = 0
    for line in f:
        total += sum(int(n) for n in re.findall(r'\d+', line))

    assert total == 2298

#assert sum(int(n) for n in re.findall(r'\d+', open('f2.txt', encoding='ascii').read())) == 2298

print('test passed')
