# <a name="number-and-string-data-types"></a>Number and String data types

* [Numbers](#numbers)
* [String](#string)
* [Constants](#constants)
* [Built-in Operators](#built-in-operators)

Variable data type is automatically determined by Python. They only need to be assigned some value before using it elsewhere - like print function or part of expression

<br>

### <a name="numbers"></a>Numbers

* Integer examples

```python
>>> num1 = 7
>>> num2 = 42
>>> total = num1 + num2
>>> print(total)
49
>>> total
49

# no limit to integer precision, only limited by available memory
>>> 34 ** 32
10170102859315411774579628461341138023025901305856

# using single / gives floating point output
>>> 9 / 5
1.8

# using double / gives only the integer portion, no rounding
>>> 9 // 5
1

>>> 9 % 5
4
```

* Floating point examples

```python
>>> appx_pi = 22 / 7
>>> appx_pi
3.142857142857143

>>> area = 42.16
>>> appx_pi + area
45.30285714285714

>>> num1
7
>>> num1 + area
49.16
```

* the [E scientific notation](https://en.wikipedia.org/wiki/Scientific_notation#E_notation) can be used as well

```python
>>> sci_num1 = 3.982e5
>>> sci_num2 = 9.32e-1
>>> sci_num1 + sci_num2
398200.932

>>> 2.13e21 + 5.23e22
5.443e+22
```

* Binary numbers are prefixed with `0b` or `0B` (i.e digit 0 followed by lower/upper case letter b)
* Octal numbers are prefixed with `0o` or `0O` (i.e digit 0 followed by lower/upper case letter o)
* Similarly, Hexadecimal numbers are prefixed with `0x` or `0X`

```python
>>> bin_num = 0b101
>>> oct_num = 0o12
>>> hex_num = 0xF

>>> bin_num
5
>>> oct_num
10
>>> hex_num
15

>>> oct_num + hex_num
25
```

* `_` can be used between digits for readability
    * introduced in Python v3.6

```python
>>> 1_000_000
1000000
>>> 1_00.3_352
100.3352
>>> 0xff_ab1
1047217

# f-strings formatting explained in a later chapter
>>> num = 34 ** 32
>>> print(f'{num:_}')
10_170_102_859_315_411_774_579_628_461_341_138_023_025_901_305_856
```

**Further Reading**

* [Python docs - numbers](https://docs.python.org/3/tutorial/introduction.html#numbers)
* [decimal](https://docs.python.org/3/library/decimal.html)
* [fractions](https://docs.python.org/3/library/fractions.html)
* [complex](https://docs.python.org/3/library/functions.html#complex)
* [Python docs - keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords) - do not use these as variables

<br>

### <a name="string"></a>String

* strings can be declared using single or double quotes
* Use `\` to escape quotes which are part of string itself if the string contains both single and double quotes

```python
>>> str1 = 'This is a string'
>>> str1
'This is a string'
>>> greeting = "Hello World!"
>>> greeting
'Hello World!'

>>> weather = "It's a nice and warm day"
>>> weather
"It's a nice and warm day"
>>> print(weather)
It's a nice and warm day

>>> weather = 'It\'s a nice and warm day'
>>> print(weather)
It's a nice and warm day
```

* Escape sequences like newline character `\n` can be used within string declaration

```python
>>> colors = 'Blue\nRed\nGreen'
>>> colors
'Blue\nRed\nGreen'

>>> print(colors)
Blue
Red
Green
```

* Use `r` prefix (stands for **raw**) if you do not want escape sequences to be interpreted
* It is commonly used with regular expressions, see [Pattern matching and extraction](./Text_Processing.md#pattern-matching-and-extraction) for examples

```bash
>>> raw_str = r'Blue\nRed\nGreen'
>>> print(raw_str)
Blue\nRed\nGreen

# to see how the string is stored internally
>>> raw_str
'Blue\\nRed\\nGreen'
```

* String concatenation and repetition

```python
>>> str1 = 'Hello'
>>> str2 = ' World'
>>> print(str1 + str2)
Hello World

>>> style_char = '-'
>>> style_char * 10
'----------'

>>> word = 'buffalo '
>>> print(word * 8)
buffalo buffalo buffalo buffalo buffalo buffalo buffalo buffalo 

# Python v3.6 allows variable interpolation with f-strings
>>> msg = f'{str1} there'
>>> msg
'Hello there'
```

* Triple quoted strings
* like single line strings, `"""` or `'''` can be used as required as well as escape characters using `\`

```python
#!/usr/bin/python3

"""
This line is part of multiline comment

This program shows examples of triple quoted strings
"""

# assigning multiple line string to variable
poem = """\
The woods are lovely, dark and deep,   
But I have promises to keep,   
And miles to go before I sleep,   
And miles to go before I sleep.
"""

print(poem, end='')
```

* Triple quoted strings also help in documentation, see [Docstrings](./Docstrings.md) chapter for examples

```
$ ./triple_quoted_string.py 
The woods are lovely, dark and deep,   
But I have promises to keep,   
And miles to go before I sleep,   
And miles to go before I sleep.
$
```

**Further Reading**

* [Python docs - strings](https://docs.python.org/3/tutorial/introduction.html#strings)
* [Python docs - f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) - for more examples and caveats
* [Python docs - List of Escape Sequences and more info on strings](https://docs.python.org/3/reference/lexical_analysis.html#strings)
* [Python docs - Binary Sequence Types](https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview)
* [formatting triple quoted strings](https://stackoverflow.com/questions/3877623/in-python-can-you-have-variables-within-triple-quotes-if-so-how)

<br>

### <a name="constants"></a>Constants

Paraphrased from [Python docs - constants](https://docs.python.org/3/library/constants.html)

* `None` The sole value of the type `NoneType`
    * `None` is frequently used to represent the absence of a value
* `False` The false value of the `bool` type
* `True` The true value of the `bool` type
* [Python docs - Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth)

```python
>>> bool(2)
True
>>> bool(0)
False
>>> bool('')
False
>>> bool('a')
True
```

<br>

### <a name="built-in-operators"></a>Built-in Operators

* arithmetic operators
    * `+` addition
    * `-` subtraction
    * `*` multiplication
    * `/` division (float output)
    * `//` division (integer output, result is not rounded)
    * `**` exponentiation
    * `%` modulo
* string operators
    * `+` string concatenation
    * `*` string repetition
* comparison operators
    * `==` equal to
    * `>` greater than
    * `<` less than
    * `!=` not equal to
    * `>=` greater than or equal to
    * `<=` less than or equal to
* boolean logic
    * `and` logical and
    * `or` logical or
    * `not` logical not
* bitwise operators
    * `&` and
    * `|` or
    * `^` exclusive or
    * `~` invert bits
    * `>>` right shift
    * `<<` left shift
* and many more...

**Further Reading**

* [Python docs - Numeric types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex) - complete list of operations and precedence
* [Python docs - String methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

