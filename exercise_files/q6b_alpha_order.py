#!/usr/bin/python3

def is_alpha_order(word):
    pass

assert is_alpha_order('bot')
assert is_alpha_order('art')
assert is_alpha_order('toe')
assert is_alpha_order('AborT')

assert not is_alpha_order('are')
assert not is_alpha_order('boat')
assert not is_alpha_order('Flee')

#sentence
def is_alpha_order_sentence(sentence):
    pass

assert is_alpha_order_sentence('Toe got bit')
assert not is_alpha_order_sentence('All is well')

print('all tests passed')
