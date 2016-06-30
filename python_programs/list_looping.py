#!/usr/bin/python3

numbers = [2, 12, 3, 25, 624, 21, 5, 9, 12]
odd_numbers  = []
even_numbers = []

for num in numbers:
    odd_numbers.append(num) if(num % 2) else even_numbers.append(num)

print("numbers:      {}".format(numbers))
print("odd_numbers:  {}".format(odd_numbers))
print("even_numbers: {}".format(even_numbers))
