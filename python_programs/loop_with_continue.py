#!/usr/bin/python3

prev_num = 0
curr_num = 0
print("The first ten numbers in fibonacci sequence: ", end='')

for num in range(10):
    print(curr_num, end=' ')

    if num == 0:
        curr_num = 1
        continue

    temp = curr_num
    curr_num = curr_num + prev_num
    prev_num = temp

print("")
