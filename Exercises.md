# <a name="exercises"></a>Exercises

* [Variables and Print](#variables-and-print)
* [Functions](#functions)
* [Control structures](#control-structures)
* [List](#list)
* [File](#file)
* [Text processing](#text-processing)
* [Misc](#misc)

<br>

## <a name="variables-and-print"></a>Variables and Print

Ask user information, for ex: `name`, `department`, `college` etc and display them using print function

```
# Sample of how program might ask user input and display output afterwards
$ ./usr_ip.py 
Please provide the following details
Enter your name: learnbyexample
Enter your department: ECE
Enter your college: PSG Tech

------------------------------------
Name       : learnbyexample
Department : ECE
College    : PSG Tech
```

<br>

## <a name="functions"></a>Functions

* Returns length of integer numbers

```python
>>> len_int(962306349871524124750813401378124)
33
>>> len_int(+42)
2
>>> len_int(-42)
3

# bonus: handle -ve numbers and check for input type
>>> len_int(-42)
2
>>> len_int('a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in len_int
TypeError: provide only integer input
```

* Returns True/False - two strings are same irrespective of lowercase/uppercase

```python
>>> str_cmp('nice', 'nice')
True
>>> str_cmp('Hi there', 'hi there')
True
>>> str_cmp('GoOd DaY', 'gOOd dAy')
True
>>> str_cmp('foo', 'food')
False
```

* Returns True/False - two strings are anagrams (assume input consists of alphabets only)

```python
>>> str_anagram('god', 'Dog')
True
>>> str_anagram('beat', 'table')
False
>>> str_anagram('beat', 'abet')
True
```

<br>

## <a name="control-structures"></a>Control structures

* Write a function that returns
    * 'Good' for numbers divisable by 7
    * 'Food' for numbers divisable by 6
    * 'Universe' for numbers divisable by 42
    * 'Oops' for all other numbers
    * Only one output, divisable by 42 takes precedence

```python
>>> six_by_seven(66)
'Food'
>>> six_by_seven(13)
'Oops'
>>> six_by_seven(42)
'Universe'
>>> six_by_seven(14)
'Good'
>>> six_by_seven(84)
'Universe'
>>> six_by_seven(235432)
'Oops'
```

*bonus*: use a loop to print number and corresponding string for numbers 1 to 100

```python
1 Oops
2 Oops
3 Oops
4 Oops
5 Oops
6 Food
7 Good
...
41 Oops
42 Universe
...
98 Good
99 Oops
100 Oops
```

* Print all numbers from 1 to 1000 which reads the same in reversed form in both binary and decimal format

```
$ ./dec_bin.py 
1 1
3 11
5 101
7 111
9 1001
33 100001
99 1100011
313 100111001
585 1001001001
717 1011001101
```

*bonus*: add octal and hexadecimal checks as well

```
$ ./dec_bin_oct.py 
1 0b1 0o1
3 0b11 0o3
5 0b101 0o5
7 0b111 0o7
9 0b1001 0o11
585 0b1001001001 0o1111

$ ./dec_bin_oct_hex.py 
1 0b1 0o1 0x1
3 0b11 0o3 0x3
5 0b101 0o5 0x5
7 0b111 0o7 0x7
9 0b1001 0o11 0x9
```

<br>

## <a name="list"></a>List

* Write a function that returns product of all numbers of a list

```python
>>> product([1, 4, 21])
84
>>> product([-4, 2.3e12, 77.23, 982, 0b101])
-3.48863356e+18
```

*bonus*: works on any kind of iterable

```python
>>> product(b)
84
>>> product((-3, 11, 2))
-66
>>> product({8, 300})
2400
>>> product([234, 121, 23, 945, 0])
0
>>> product(range(2, 6))
120
# can you identify what mathematical function the last one performs?
```

* Write a function that returns 3rd lowest number of a list (or iterable in general)

```python
>>> third_lowest([42, 23421341, 234.2e3, 21, 232, 12312, -2343])
42
>>> third_lowest([1, -2, 4, 2, 1, 3, 3, 5])
2

>>> third_lowest('unrecognizable')
'c'

>>> third_lowest([121, 782])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in third_lowest
IndexError: list index out of range
```

<br>

## <a name="file"></a>File

* Print sum of all numbers from a file
	* file containing only single column and all numbers
	* file containing arbitary string with numbers interspersed

<br>

## <a name="text-processing"></a>Text processing

* Function to check if two words are same or differ by only one character. For ex: bar
 	* would match with baz, bat, bar, car, etc
 	* not match bark, art, bot, etc
* Check if a word is in ascending alphabetic order or not
* Check if a word is in either ascending or descending alphabetic order

<br>

## <a name="misc"></a>Misc

* Play a song
* Open college website

