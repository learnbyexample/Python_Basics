#!/usr/bin/python3

def is_one_char_diff(word1, word2):
    pass

assert is_one_char_diff('bar', 'car')
assert is_one_char_diff('bar', 'Bat')
assert is_one_char_diff('bar', 'bar')
assert is_one_char_diff('bar', 'baZ')
assert is_one_char_diff('A', 'b')

assert not is_one_char_diff('a', '')
assert not is_one_char_diff('bar', 'bark')
assert not is_one_char_diff('bar', 'Art')
assert not is_one_char_diff('bar', 'bot')
assert not is_one_char_diff('ab', '')

assert is_one_char_diff('Food', 'good')
assert is_one_char_diff('food', 'fold')
assert not is_one_char_diff('food', 'Foody')
assert not is_one_char_diff('food', 'fled')

print('all tests passed')
