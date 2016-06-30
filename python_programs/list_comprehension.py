#!/usr/bin/python3

import time

numbers = list(range(1,100001))
fl_square_numbers = []

# reference time
t0 = time.perf_counter()

# ------------ for loop ------------
for num in numbers:
    fl_square_numbers.append(num * num)

# reference time
t1 = time.perf_counter()

# ------- list comprehension -------
lc_square_numbers = [num * num for num in numbers]

# performance results
t2 = time.perf_counter()
fl_time = t1 - t0
lc_time = t2 - t1
improvement = (fl_time - lc_time) / fl_time * 100

print("Time with for loop:           {:.4f}".format(fl_time))
print("Time with list comprehension: {:.4f}".format(lc_time))
print("Improvement:                  {:.2f}%".format(improvement))

if fl_square_numbers == lc_square_numbers:
    print("\nfl_square_numbers and lc_square_numbers are equivalent")
else:
    print("\nfl_square_numbers and lc_square_numbers are NOT equivalent")
