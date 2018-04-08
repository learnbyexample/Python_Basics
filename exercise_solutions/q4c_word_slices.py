#!/usr/bin/python3

def word_slices(s):
    size = len(s)
    if size < 3:
        return [s]
    return [s[i:j+1] for i in range(size-1) for j in range(i+1, size)]

assert word_slices('i') == ["i"]
assert word_slices('to') == ["to"]
assert word_slices('are') == ["ar", "are", "re"]
assert word_slices('boat') == ["bo", "boa", "boat", "oa", "oat", "at"]
assert word_slices('table') == ["ta", "tab", "tabl", "table", "ab",
                                      "abl", "able", "bl", "ble", "le"]

print('all tests passed')
