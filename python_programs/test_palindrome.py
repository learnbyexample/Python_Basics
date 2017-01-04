#!/usr/bin/python3

import palindrome

assert palindrome.is_palindrome('Madam')
assert palindrome.is_palindrome("Dammit, I'm mad!")
assert not palindrome.is_palindrome('aaa')
assert palindrome.is_palindrome('Malayalam')

try:
    assert palindrome.is_palindrome('as2')
except ValueError as e:
    assert str(e) == 'Characters other than alphabets and punctuations'

try:
    assert palindrome.is_palindrome("a'a")
except ValueError as e:
    assert str(e) == 'Less than 3 alphabets'

print('All tests passed')
