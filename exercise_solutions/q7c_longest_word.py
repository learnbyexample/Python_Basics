#!/usr/bin/python3

import urllib.request, re

def longest_word(ip, url=False):
    if url:
        ip_data = urllib.request.urlopen(ip).read().decode('utf-8')
    else:
        ip_data = open(ip, encoding='utf-8').read()

    return sorted(re.findall(r'[a-zA-Z]+', ip_data), key=len)[-1]

ip_path = 'poem.txt'
assert longest_word(ip_path) == 'Violets'

# The Scarlet Pimpernel
ip_path = 'https://www.gutenberg.org/files/60/60.txt'
assert longest_word(ip_path, True) == 'misunderstandings'

print('all tests passed')

