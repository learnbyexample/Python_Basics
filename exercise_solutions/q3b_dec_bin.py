#!/usr/bin/python3

for n in range(1, 1001):
    dec_n = str(n)
    bin_n = format(n, 'b')
    if dec_n == dec_n[::-1] and bin_n == bin_n[::-1]:
        print(dec_n, bin_n)

    #oct_n = format(n, 'o')
    #if dec_n == dec_n[::-1] and bin_n == bin_n[::-1] and oct_n == oct_n[::-1]:
    #    print('{0:d} {0:#b} {0:#o}'.format(n))

    #oct_n = format(n, 'o')
    #hex_n = format(n, 'x')
    ##if all((dec_n == dec_n[::-1], bin_n == bin_n[::-1], oct_n == oct_n[::-1], hex_n == hex_n[::-1])):
    #if dec_n == dec_n[::-1] and bin_n == bin_n[::-1] and \
    #   oct_n == oct_n[::-1] and hex_n == hex_n[::-1]:
    #    print('{0:d} {0:#b} {0:#o} {0:#x}'.format(n))
