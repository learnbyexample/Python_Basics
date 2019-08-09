# <a name="text-processing"></a>Text Processing

* [String methods](#string-methods)
* [Regular Expressions](#regular-expressions)
* [Pattern matching and extraction](#pattern-matching-and-extraction)
* [Search and Replace](#search-and-replace)
* [Compiling Regular Expressions](#compiling-regular-expressions)
* [Further Reading on Regular Expressions](#further-reading-on-regular-expressions)

<br>

### <a name="string-methods"></a>String methods

* translate string characters
    * `str.maketrans()` to get translation table
    * `translate()` to perform the string mapping based on translation table
* the first argument to `maketrans()` is string characters to be replaced, the second is characters to replace with and the third is characters to be mapped to `None`
* [character translation examples](https://stackoverflow.com/questions/555705/character-translation-using-python-like-the-tr-command)

```python
>>> greeting = '===== Have a great day ====='
>>> greeting.translate(str.maketrans('=', '-'))
'----- Have a great day -----'

>>> greeting = '===== Have a great day!! ====='
>>> greeting.translate(str.maketrans('=', '-', '!'))
'----- Have a great day -----'

>>> import string
>>> quote = 'SIMPLICITY IS THE ULTIMATE SOPHISTICATION'
>>> tr_table = str.maketrans(string.ascii_uppercase, string.ascii_lowercase)
>>> quote.translate(tr_table)
'simplicity is the ultimate sophistication'

>>> sentence = "Thi1s is34 a senten6ce"
>>> sentence.translate(str.maketrans('', '', string.digits))
'This is a sentence'
>>> greeting.translate(str.maketrans('', '', string.punctuation))
' Have a great day '
```

* removing leading/trailing/both characters
* only consecutive characters from start/end string are removed
* by default whitespace characters are stripped
* if more than one character is specified, it is treated as a set and all combinations of it are used

```python
>>> greeting = '      Have a nice day :)     '
>>> greeting.strip()
'Have a nice day :)'
>>> greeting.rstrip()
'      Have a nice day :)'
>>> greeting.lstrip()
'Have a nice day :)     '

>>> greeting.strip(') :')
'Have a nice day'

>>> greeting = '===== Have a great day!! ====='
>>> greeting.strip('=')
' Have a great day!! '
```

* styling
* width argument specifies total output string length

```python
>>> ' Hello World '.center(40, '*')
'************* Hello World **************'
```

* changing case and case checking

```python
>>> sentence = 'thIs iS a saMple StrIng'

>>> sentence.capitalize()
'This is a sample string'

>>> sentence.title()
'This Is A Sample String'

>>> sentence.lower()
'this is a sample string'

>>> sentence.upper()
'THIS IS A SAMPLE STRING'

>>> sentence.swapcase()
'THiS Is A SAmPLE sTRiNG'

>>> 'good'.islower()
True

>>> 'good'.isupper()
False
```

* check if string is made up of numbers

```python
>>> '1'.isnumeric()
True
>>> 'abc1'.isnumeric()
False
>>> '1.2'.isnumeric()
False
```

* check if character sequence is present or not

```python
>>> sentence = 'This is a sample string'
>>> 'is' in sentence
True
>>> 'this' in sentence
False
>>> 'This' in sentence
True
>>> 'this' in sentence.lower()
True
>>> 'is a' in sentence
True
>>> 'test' not in sentence
True
```

* get number of times character sequence is present (non-overlapping)

```python
>>> sentence = 'This is a sample string'
>>> sentence.count('is')
2
>>> sentence.count('w')
0

>>> word = 'phototonic'
>>> word.count('oto')
1
```

* matching character sequence at start/end of string

```python
>>> sentence
'This is a sample string'

>>> sentence.startswith('This')
True
>>> sentence.startswith('The')
False

>>> sentence.endswith('ing')
True
>>> sentence.endswith('ly')
False
```

* split string based on character sequence
* returns a list
* to split using regular expressions, use `re.split()` instead

```python
>>> sentence = 'This is a sample string'

>>> sentence.split()
['This', 'is', 'a', 'sample', 'string']

>>> "oranges:5".split(':') 
['oranges', '5']
>>> "oranges :: 5".split(' :: ') 
['oranges', '5']

>>> "a e i o u".split(' ', maxsplit=1) 
['a', 'e i o u']
>>> "a e i o u".split(' ', maxsplit=2) 
['a', 'e', 'i o u']

>>> line = '{1.0 2.0 3.0}'
>>> nums = [float(s) for s in line.strip('{}').split()]
>>> nums
[1.0, 2.0, 3.0]
```

* joining list of strings

```python
>>> str_list
['This', 'is', 'a', 'sample', 'string']
>>> ' '.join(str_list)
'This is a sample string'
>>> '-'.join(str_list)
'This-is-a-sample-string'

>>> c = ' :: '
>>> c.join(str_list)
'This :: is :: a :: sample :: string'
```

* replace characters
* third argument specifies how many times replace has to be performed
* variable has to be explicitly re-assigned to change its value

```python
>>> phrase = '2 be or not 2 be'
>>> phrase.replace('2', 'to')
'to be or not to be'

>>> phrase
'2 be or not 2 be'

>>> phrase.replace('2', 'to', 1)
'to be or not 2 be'

>>> phrase = phrase.replace('2', 'to')
>>> phrase
'to be or not to be'
```

**Further Reading**

* [Python docs - string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
* [python string methods tutorial](http://www.thehelloworldprogram.com/python/python-string-methods/)

<br>

### <a name="regular-expressions"></a>Regular Expressions

* Handy reference of regular expression (RE) elements

| Meta characters | Description |
| ------------- | ----------- |
| `\A` | anchor to restrict matching to beginning of string |
| `\Z` | anchor to restrict matching to end of string |
| `^` | anchor to restrict matching to beginning of line |
| `$` | anchor to restrict matching to end of line |
| `.` | Match any character except newline character `\n` |
| &#124; | OR operator for matching multiple patterns |
| `(RE)` | capturing group |
| `(?:RE)` | non-capturing group |
| `[]` | Character class - match one character among many |
| `\^` | prefix `\` to literally match meta characters like `^` |

<br>

| Greedy Quantifiers | Description |
| ------------- | ----------- |
| `*` | Match zero or more times |
| `+` | Match one or more times |
| `?` | Match zero or one times |
| `{m,n}` | Match `m` to `n` times (inclusive) |
| `{m,}` | Match at least m times |
| `{,n}` | Match up to `n` times (including `0` times) |
| `{n}` | Match exactly n times |

Appending a `?` to greedy quantifiers makes them non-greedy

<br>

| Character classes | Description |
| ------------- | ----------- |
| `[aeiou]` | Match any vowel |
| `[^aeiou]` | `^` inverts selection, so this matches any consonant |
| `[a-f]` | `-` defines a range, so this matches any of abcdef characters |
| `\d` | Match a digit, same as `[0-9]` |
| `\D` | Match non-digit, same as `[^0-9]` or `[^\d]` |
| `\w` | Match alphanumeric and underscore character, same as `[a-zA-Z0-9_]` |
| `\W` | Match non-alphanumeric and underscore character, same as `[^a-zA-Z0-9_]` or `[^\w]` |
| `\s` | Match white-space character, same as `[\ \t\n\r\f\v]` |
| `\S` | Match non white-space character, same as `[^\s]` |
| `\b` | word boundary, see `\w` for characters constituting a word |
| `\B` | not a word boundary |

<br>

| Flags | Description |
| ------------- | ----------- |
| `re.I` | Ignore case |
| `re.M` | Multiline mode, `^` and `$` anchors work on lines |
| `re.S` | Singleline mode, `.` will also match `\n` |
| `re.X` | Verbose mode, for better readability and adding comments |

See [Python docs - Compilation Flags](https://docs.python.org/3/howto/regex.html#compilation-flags) for more details and long names for flags

<br>

| Variable | Description |
| ------------- | ----------- |
| `\1`, `\2`, `\3` ... `\99` | backreferencing matched patterns |
| `\g<1>`, `\g<2>`, `\g<3>` ... | backreferencing matched patterns, prevents ambiguity |
| `\g<0>` | entire matched portion |

`\0` and `\100` onwards are considered as octal values, hence cannot be used as backreference.

<br>

### <a name="pattern-matching-and-extraction"></a>Pattern matching and extraction

To match/extract sequence of characters, use

* `re.search()` to see if input string contains a pattern or not
* `re.findall()` to get a list of all matching portions
* `re.finditer()` to get an iterator of `re.Match` objects of all matching portions
* `re.split()` to get a list from splitting input string based on a pattern

Their syntax is as follows:

```python
re.search(pattern, string, flags=0)
re.findall(pattern, string, flags=0)
re.finditer(pattern, string, flags=0)
re.split(pattern, string, maxsplit=0, flags=0)
```

* As a good practice, always use **raw strings** to construct RE, unless other formats are required 
    * this will avoid clash of backslash escaping between RE and normal quoted strings
* examples for `re.search`

```python
>>> sentence = 'This is a sample string'

# using normal string methods
>>> 'is' in sentence
True
>>> 'xyz' in sentence
False

# need to load the re module before use
>>> import re
# check if 'sentence' contains the pattern described by RE argument
>>> bool(re.search(r'is', sentence))
True
>>> bool(re.search(r'this', sentence, flags=re.I))
True
>>> bool(re.search(r'xyz', sentence))
False
```

* examples for `re.findall`

```python
# match whole word par with optional s at start and e at end
>>> re.findall(r'\bs?pare?\b', 'par spar apparent spare part pare')
['par', 'spar', 'spare', 'pare']

# numbers >= 100 with optional leading zeros
>>> re.findall(r'\b0*[1-9]\d{2,}\b', '0501 035 154 12 26 98234')
['0501', '154', '98234']

# if multiple capturing groups are used, each element of output
# will be a tuple of strings of all the capture groups
>>> re.findall(r'(x*):(y*)', 'xx:yyy x: x:yy :y')
[('xx', 'yyy'), ('x', ''), ('x', 'yy'), ('', 'y')]

# normal capture group will hinder ability to get whole match
# non-capturing group to the rescue
>>> re.findall(r'\b\w*(?:st|in)\b', 'cost akin more east run against')
['cost', 'akin', 'east', 'against']

# useful for debugging purposes as well before applying substitution
>>> re.findall(r't.*?a', 'that is quite a fabricated tale')
['tha', 't is quite a', 'ted ta']
```

* examples for `re.split`

```python
# split based on one or more digit characters
>>> re.split(r'\d+', 'Sample123string42with777numbers')
['Sample', 'string', 'with', 'numbers']

# split based on digit or whitespace characters
>>> re.split(r'[\d\s]+', '**1\f2\n3star\t7 77\r**')
['**', 'star', '**']

# to include the matching delimiter strings as well in the output
>>> re.split(r'(\d+)', 'Sample123string42with777numbers')
['Sample', '123', 'string', '42', 'with', '777', 'numbers']

# use non-capturing group if capturing is not needed
>>> re.split(r'hand(?:y|ful)', '123handed42handy777handful500')
['123handed42', '777', '500']
```

* backreferencing

```python
# whole words that have at least one consecutive repeated character
>>> words = ['effort', 'flee', 'facade', 'oddball', 'rat', 'tool']

>>> [w for w in words if re.search(r'\b\w*(\w)\1\w*\b', w)]
['effort', 'flee', 'oddball', 'tool']
```

* The `re.search` function returns a `re.Match` object from which various details can be extracted
like the matched portion of string, location of matched portion, etc
* **Note** that output here is shown for Python version **3.7**

```python
>>> re.search(r'b.*d', 'abc ac adc abbbc')
<re.Match object; span=(1, 9), match='bc ac ad'>
# retrieving entire matched portion
>>> re.search(r'b.*d', 'abc ac adc abbbc')[0]
'bc ac ad'

# capture group example
>>> m = re.search(r'a(.*)d(.*a)', 'abc ac adc abbbc')
# to get matched portion of second capture group
>>> m[2]
'c a'
# to get a tuple of all the capture groups
>>> m.groups()
('bc ac a', 'c a')
```

* examples for `re.finditer`

```python
>>> m_iter = re.finditer(r'(x*):(y*)', 'xx:yyy x: x:yy :y')
>>> [(m[1], m[2]) for m in m_iter]
[('xx', 'yyy'), ('x', ''), ('x', 'yy'), ('', 'y')]

>>> m_iter = re.finditer(r'ab+c', 'abc ac adc abbbc')
>>> for m in m_iter:
...     print(m.span())
... 
(0, 3)
(11, 16)
```

<br>

### <a name="search-and-replace"></a>Search and Replace

**Syntax**

```python
re.sub(pattern, repl, string, count=0, flags=0)
```

* examples
* **Note** that as strings are immutable, `re.sub` will not change value of variable
passed to it, has to be explicity assigned

```python
>>> ip_lines = "catapults\nconcatenate\ncat"
>>> print(re.sub(r'^', r'* ', ip_lines, flags=re.M))
* catapults
* concatenate
* cat

# replace 'par' only at start of word
>>> re.sub(r'\bpar', r'X', 'par spar apparent spare part')
'X spar apparent spare Xt'

# same as: r'part|parrot|parent'
>>> re.sub(r'par(en|ro)?t', r'X', 'par part parrot parent')
'par X X X'

# remove first two columns where : is delimiter
>>> re.sub(r'\A([^:]+:){2}', r'', 'foo:123:bar:baz', count=1)
'bar:baz'
```

* backreferencing

```python
# remove any number of consecutive duplicate words separated by space
# quantifiers can be applied to backreferences too!
>>> re.sub(r'\b(\w+)( \1)+\b', r'\1', 'aa a a a 42 f_1 f_1 f_13.14')
'aa a 42 f_1 f_13.14'

# add something around the matched strings
>>> re.sub(r'\d+', r'(\g<0>0)', '52 apples and 31 mangoes')
'(520) apples and (310) mangoes'

# swap words that are separated by a comma
>>> re.sub(r'(\w+),(\w+)', r'\2,\1', 'a,b 42,24')
'b,a 24,42'
```

* using functions in replace part of `re.sub()`
* **Note** that Python version **3.7** is used here

```python
>>> from math import factorial
>>> numbers = '1 2 3 4 5'
>>> def fact_num(n):
...     return str(factorial(int(n[0])))
... 
>>> re.sub(r'\d+', fact_num, numbers)
'1 2 6 24 120'

# using lambda
>>> re.sub(r'\d+', lambda m: str(factorial(int(m[0]))), numbers)
'1 2 6 24 120'
```

* [call functions from re.sub](https://stackoverflow.com/questions/11944978/call-functions-from-re-sub)
* [replace string pattern with output of function](https://stackoverflow.com/questions/12597370/python-replace-string-pattern-with-output-of-function)
* [lambda tutorial](https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/)

<br>

### <a name="compiling-regular-expressions"></a>Compiling Regular Expressions

* Regular expressions can be compiled using `re.compile` function, which gives back a
`re.Pattern` object
* The top level `re` module functions are all available as methods for this object
* Compiling a regular expression helps if the RE has to be used in multiple
places or called upon multiple times inside a loop (speed benefit)
* By default, Python maintains a small list of recently used RE, so the speed benefit
doesn't apply for trivial use cases

```python
>>> pet = re.compile(r'dog')
>>> type(pet)
<class 're.Pattern'>
>>> bool(pet.search('They bought a dog'))
True
>>> bool(pet.search('A cat crossed their path'))
False

>>> remove_parentheses = re.compile(r'\([^)]*\)')
>>> remove_parentheses.sub('', 'a+b(addition) - foo() + c%d(#modulo)')
'a+b - foo + c%d'
>>> remove_parentheses.sub('', 'Hi there(greeting). Nice day(a(b)')
'Hi there. Nice day'
```

<br>

### <a name="further-reading-on-regular-expressions"></a>Further Reading on Regular Expressions

* [Python re(gex)?](https://github.com/learnbyexample/py_regular_expressions) - a book on regular expressions
* [Python docs - re module](https://docs.python.org/3/library/re.html)
* [Python docs - introductory tutorial to using regular expressions](https://docs.python.org/3/howto/regex.html)
* [Comprehensive reference: What does this regex mean?](https://stackoverflow.com/questions/22937618/reference-what-does-this-regex-mean)
* [rexegg](https://www.rexegg.com/) - tutorials, tricks and more
* [regular-expressions](https://www.regular-expressions.info/) - tutorials and tools
* [CommonRegex](https://github.com/madisonmay/CommonRegex) - collection of common regular expressions
* Practice tools
    * [regex101](https://regex101.com/) - visual aid and online testing tool for regular expressions, select flavor as Python before use
    * [debuggex](https://www.debuggex.com) - railroad diagrams for regular expressions, select flavor as Python before use
    * [regexone](https://regexone.com/) - interative tutorial
	* [cheatsheet](https://www.shortcutfoo.com/app/dojos/python-regex/cheatsheet) - one can also learn it [interactively](https://www.shortcutfoo.com/app/dojos/python-regex)
    * [regexcrossword](https://regexcrossword.com/) - practice by solving crosswords, read 'How to play' section before you start

