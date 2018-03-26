#!/usr/bin/python3

with open('f1.txt', 'r', encoding='ascii') as f:
    total = 0
    for line in f:
        total += float(line)

    assert total == 10485.14

print('test passed')

# for small files that can fit in memory
#total = sum(float(n) for n in open('f1.txt', encoding='ascii').readlines())
