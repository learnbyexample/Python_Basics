#!/usr/bin/python3

def longest_word():
    pass

ip_path = 'poem.txt'
assert longest_word(ip_path) == 'Violets'

# The Scarlet Pimpernel
ip_path = 'https://www.gutenberg.org/files/60/60.txt'
assert longest_word(ip_path, True) == 'misunderstandings'

print('all tests passed')

