#!/usr/bin/python3

def max_nested_braces(expr):
    pass

assert max_nested_braces('a*b') == 0
assert max_nested_braces('a*b{') == -1
assert max_nested_braces('a*{b+c}') == 1
assert max_nested_braces('{a+2}*{b+c}') == 1
assert max_nested_braces('a*{b+c*{e*3.14}}') == 2
assert max_nested_braces('a*{b+c*{e*3.14}}}') == -1
assert max_nested_braces('a*{b+c}}') == -1
assert max_nested_braces('a*b+{}') == 1
assert max_nested_braces('}a+b{') == -1
assert max_nested_braces('{{a+2}*{b+c}+e}') == 2
assert max_nested_braces('{{a+2}*{b+{c*d}}+e}') == 3
assert max_nested_braces('{{a+2}*{{b+{c*d}}+e*d}}') == 4
assert max_nested_braces('{{a+2}*{{b}+{c*d}}+e*d}}') == -1

print('all tests passed')


#### alternate using regular expressions

#import re
#
#def max_nested_braces(expr):
#    count = 0
#    while True:
#        expr_sub = re.sub(r'\{[^{}]*\}', '', expr)
#        if expr_sub == expr:
#            break
#        count += 1
#        expr = expr_sub
#
#    if re.search(r'[{}]', expr):
#        return -1
#    return count

# for bonus, use + instead of *
#assert max_nested_braces('a*b+{}') == -1
#assert max_nested_braces('a*{b+{}+c*{e*3.14}}') == -1
