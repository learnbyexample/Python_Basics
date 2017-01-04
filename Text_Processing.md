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
    * `maketrans()` to get translation table
    * `translate()` to perform the string mapping based on translation table
* the first argument to `maketrans()` is string characters to be replaced, the second is characters to replace with and the third is characters to be mapped to `None`
* [character translation examples](https://stackoverflow.com/questions/555705/character-translation-using-python-like-the-tr-command)

```python
>>> greeting = '===== Have a great day ====='
>>> greeting.translate(greeting.maketrans('=','-'))
'----- Have a great day -----'

>>> greeting = '===== Have a great day!! ====='
>>> greeting.translate(greeting.maketrans('=','-', '!'))
'----- Have a great day -----'

>>> import string
>>> quote = 'SIMPLICITY IS THE ULTIMATE SOPHISTICATION'
>>> tr_table = quote.maketrans(string.ascii_uppercase,string.ascii_lowercase)
>>> quote.translate(tr_table)
'simplicity is the ultimate sophistication'

>>> sentence = "Thi1s is34 a senten6ce"
>>> sentence.translate(sentence.maketrans('', '', string.digits))
'This is a sentence'
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

>>> line = '(1.0 2.0 3.0)'
>>> nums = [float(s) for s in line.strip('()').split()]
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
>>> '--'.join(str_list)
'This--is--a--sample--string'
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

* Handy reference of regular expression elements

| Meta characters | Description |
| ------------- | ----------- |
| ^ | anchor, match from beginning of string |
| $ | anchor, match end of string |
| . | Match any character except newline character \n |
| \| | OR operator for matching multiple patterns |
| () | for grouping patterns and also extraction |
| [] | Character class - match one character among many |
| \\^ | use \ to match meta characters like ^ |

<br>

| Quantifiers | Description |
| ------------- | ----------- |
| * | Match zero or more times the preceding character |
| + | Match one or more times the preceding character |
| ? | Match zero or one times the preceding character |
| {n} | Match exactly n times |
| {n,} | Match at least n times |
| {n,m} | Match at least n times but not more than m times |

<br>

| Character classes | Description |
| ------------- | ----------- |
| [aeiou] | Match any vowel |
| [^aeiou] | ^ inverts selection, so this matches any consonant |
| [a-f] | Match any of abcdef character |
| \d | Match a digit, same as [0-9] |
| \D | Match non-digit, same as [^0-9] or [^\d] |
| \w | Match alphanumeric and underscore character, same as [a-zA-Z_] |
| \W | Match non-alphanumeric and underscore character, same as [^a-zA-Z_] or [^\w] |
| \s | Match white-space character, same as [\ \t\n\r\f\v] |
| \S | Match non white-space character, same as [^\s] |
| \b | word boundary, word defined as sequence of alphanumeric characters |
| \B | not a word boundary |

<br>

| Compilation Flags | Description |
| ------------- | ----------- |
| re.I | ignore case |
| re.M | multiline mode, ^ and $ anchors work on internal lines |
| re.S | singleline mode, . will also match \n |
| re.V | verbose mode, for better readability and adding comments |

* [Python docs - Compilation Flags](https://docs.python.org/3/howto/regex.html#compilation-flags) - for more details and long names for flags

<br>

| Variable | Description |
| ------------- | ----------- |
| \1, \2, \3 etc | backreferencing matched patterns |
| \g<1>, \g<2>, \g<3> etc | backreferencing matched patterns, useful to differentiate numbers and backreferencing |

<br>
### <a name="pattern-matching-and-extraction"></a>Pattern matching and extraction

* matching/extracting sequence of characters
* use `re.search()` to see if a string contains a pattern or not
* use `re.findall()` to get a list of matching patterns
* use `re.split()` to get a list from splitting a string based on a pattern
* their syntax given below

```python
re.search(pattern, string, flags=0)
re.findall(pattern, string, flags=0)
re.split(pattern, string, maxsplit=0, flags=0)
```

```python
>>> import re
>>> string = "This is a sample string"

>>> bool(re.search('is', string))
True

>>> bool(re.search('this', string))
False

>>> bool(re.search('this', string, re.I))
True

>>> bool(re.search('T', string))
True

>>> bool(re.search('is a', string))
True

>>> re.findall('i', string)
['i', 'i', 'i']
```

* using regular expressions
* use the `r''` format when using regular expression elements

```python
>>> string
'This is a sample string'

>>> re.findall('is', string)
['is', 'is']

>>> re.findall('\bis', string)
[]

>>> re.findall(r'\bis', string)
['is']

>>> re.findall(r'\w+', string)
['This', 'is', 'a', 'sample', 'string']

>>> re.split(r'\s+', string)
['This', 'is', 'a', 'sample', 'string']

>>> re.split(r'\d+', 'Sample123string54with908numbers')
['Sample', 'string', 'with', 'numbers']

>>> re.split(r'(\d+)', 'Sample123string54with908numbers')
['Sample', '123', 'string', '54', 'with', '908', 'numbers']
```

* backreferencing

```python
>>> quote = "So many books, so little time"

>>> re.search(r'([a-z]{2,}).*\1', quote, re.I)
<_sre.SRE_Match object; span=(0, 17), match='So many books, so'>

>>> re.search(r'([a-z])\1', quote, re.I)
<_sre.SRE_Match object; span=(9, 11), match='oo'>

>>> re.findall(r'([a-z])\1', quote, re.I)
['o', 't']
```

<br>
### <a name="search-and-replace"></a>Search and Replace

**Syntax**

```python
re.sub(pattern, repl, string, count=0, flags=0)
```

* simple substitutions
* `re.sub` will not change value of variable passed to it, has to be explicity assigned

```python
>>> sentence = 'This is a sample string'
>>> re.sub('sample', 'test', sentence)
'This is a test string'

>>> sentence
'This is a sample string'
>>> sentence = re.sub('sample', 'test', sentence)
>>> sentence
'This is a test string'

>>> re.sub('/', '-', '25/06/2016')
'25-06-2016'
>>> re.sub('/', '-', '25/06/2016', count=1)
'25-06/2016'

>>> greeting = '***** Have a great day *****'
>>> re.sub('\*', '=', greeting)
'===== Have a great day ====='
```

* backreferencing

```python
>>> words = 'night and day'
>>> re.sub(r'(\w+)( \w+ )(\w+)', r'\3\2\1', words)
'day and night'

>>> line = 'Can you spot the the mistakes? I i seem to not'
>>> re.sub(r'\b(\w+) \1\b', r'\1', line, flags=re.I)
'Can you spot the mistakes? I seem to not'
```

* using functions in replace part of `re.sub()`

```python
>>> import math
>>> numbers = '1 2 3 4 5'

>>> def fact_num(n):
...     return str(math.factorial(int(n.group(1))))
... 
>>> re.sub(r'(\d+)', fact_num, numbers)
'1 2 6 24 120'

>>> re.sub(r'(\d+)', lambda m: str(math.factorial(int(m.group(1)))), numbers)
'1 2 6 24 120'
```

* [call functions from re.sub](https://stackoverflow.com/questions/11944978/call-functions-from-re-sub)
* [replace string pattern with output of function](https://stackoverflow.com/questions/12597370/python-replace-string-pattern-with-output-of-function)
* [lambda tutorial](https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/)

<br>
### <a name="compiling-regular-expressions"></a>Compiling Regular Expressions

```python
>>> swap_words = re.compile(r'(\w+)( \w+ )(\w+)')
>>> swap_words
re.compile('(\\w+)( \\w+ )(\\w+)')

>>> words = 'night and day'

>>> swap_words.search(words).group()
'night and day'
>>> swap_words.search(words).group(1)
'night'
>>> swap_words.search(words).group(2)
' and '
>>> swap_words.search(words).group(3)
'day'
>>> swap_words.search(words).group(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: no such group

>>> bool(swap_words.search(words))
True
>>> swap_words.findall(words)
[('night', ' and ', 'day')]

>>> swap_words.sub(r'\3\2\1', words)
'day and night'
>>> swap_words.sub(r'\3\2\1', 'yin and yang')
'yang and yin'
```

<br>
### <a name="further-reading-on-regular-expressions"></a>Further Reading on Regular Expressions

* [Python docs - re module](https://docs.python.org/3/library/re.html)
* [Python docs - introductory tutorial to using regular expressions](https://docs.python.org/3/howto/regex.html)
* [developers.google - Regular Expressions tutorial](https://developers.google.com/edu/python/regular-expressions)
* [automatetheboringstuff - Regular Expressions](https://automatetheboringstuff.com/chapter7/)
* [Comprehensive reference: What does this regex mean?](https://stackoverflow.com/questions/22937618/reference-what-does-this-regex-mean)
* Practice tools
    * [online regex tester](https://regex101.com/#python) shows explanations, has reference guides and ability to save and share regex
    * [regexone](http://regexone.com/) - interative tutorial
	* [cheatsheet](https://www.shortcutfoo.com/app/dojos/python-regex/cheatsheet) - one can also learn it [interactively](https://www.shortcutfoo.com/app/dojos/python-regex)
    * [regexcrossword](https://regexcrossword.com/) - practice by solving crosswords, read 'How to play' section before you start

