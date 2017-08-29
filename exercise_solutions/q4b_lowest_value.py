#!/usr/bin/python3

def nth_lowest(ip_iterable, n=1):
    return sorted(set(ip_iterable))[n-1]

nums = [42, 23421341, 234.2e3, 21, 232, 12312, -2343]
assert nth_lowest(nums, 3) == 42
assert nth_lowest(nums, 5) == 12312

nums = [1, -2, 4, 2, 1, 3, 3, 5]
assert nth_lowest(nums) == -2
assert nth_lowest(nums, 4) == 3

assert nth_lowest('unrecognizable', 3) == 'c'

print('all tests passed')
