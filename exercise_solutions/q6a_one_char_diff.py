#!/usr/bin/python3

def is_one_char_diff(word1, word2):
    if len(word1) != len(word2):
        return False

    word1, word2 = word1.lower(), word2.lower()
    for i in range(len(word1)):
        if word1[0:i] + word1[i+1:] == word2[0:i] + word2[i+1:]:
            return True

    return False

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
