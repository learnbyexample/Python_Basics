#!/usr/bin/python3

def six_by_seven(num):
    if num % 42 == 0:
        return 'Universe'
    elif num % 7 == 0:
        return 'Good'
    elif num % 6 == 0:
        return 'Food'
    else:
        return 'Oops'

assert six_by_seven(66) == 'Food'
assert six_by_seven(13) == 'Oops'
assert six_by_seven(42) == 'Universe'
assert six_by_seven(14) == 'Good'
assert six_by_seven(84) == 'Universe'
assert six_by_seven(235432) == 'Oops'

print('all tests passed')

## bonus
#for num in range(1, 101):
#    if num % 42 == 0:
#        print(num, 'Universe')
#    elif num % 7 == 0:
#        print(num, 'Good')
#    elif num % 6 == 0:
#        print(num, 'Food')
#    else:
#        print(num, 'Oops')
