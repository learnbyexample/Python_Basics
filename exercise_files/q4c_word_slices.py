#!/usr/bin/python3

def word_slices(s):
    pass

assert word_slices('i') == ["i"]
assert word_slices('to') == ["to"]
assert word_slices('are') == ["ar", "are", "re"]
assert word_slices('boat') == ["bo", "boa", "boat", "oa", "oat", "at"]
assert word_slices('table') == ["ta", "tab", "tabl", "table", "ab",
                                      "abl", "able", "bl", "ble", "le"]

print('all tests passed')
