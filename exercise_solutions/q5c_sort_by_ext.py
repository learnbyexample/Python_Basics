#!/usr/bin/python3

def sort_by_ext(ip):
    lines = open(ip, encoding='ascii').readlines()
    return sorted(lines, key=lambda x: (x.split('.')[-1].lower(), x.lower()))

exp_op = ['Fav_books\n', 'list\n', 'power.Log\n',
          'report_12.log\n', 'hello.RB\n', 'loop.do.rb\n',
          'baz.TXT\n', 'foo.123.txt\n']

assert sort_by_ext('f3.txt') == exp_op

print('test passed')

