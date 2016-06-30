#!/usr/bin/python3

# open file, read line by line and print it
filename = 'hello_world.py'
f = open(filename, 'r', encoding='ascii')

print("Contents of " + filename)
print('-' * 30)
for line in f:
    print(line, end='')

f.close()

# 'with' is a simpler alternative, automatically handles file closing
filename = 'while_loop.py'

print("\n\nContents of " + filename)
print('-' * 30)
with open(filename, 'r', encoding='ascii') as f:
    for line in f:
        print(line, end='')
