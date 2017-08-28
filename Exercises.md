# <a name="exercises"></a>Exercises

1) [Variables and Print](#variables-and-print)
2) [Functions](#functions)
3) [Control structures](#control-structures)
4) [List](#list)
5) [File](#file)
6) [Text processing](#text-processing)
7) [Misc](#misc)

<br>

For some questions, Python program with assert statements is provided to automatically test your solution in the [exercise_files](https://github.com/learnbyexample/Python_Basics/tree/master/exercise_files) directory - for ex: [Q2a - length of integer numbers](https://github.com/learnbyexample/Python_Basics/blob/master/exercise_files/q2a_int_length.py). The directory also has sample input text files.

<br>

## <a name="variables-and-print"></a>1) Variables and Print

**Q1a)** Ask user information, for ex: `name`, `department`, `college` etc and display them using print function

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

## <a name="functions"></a>2) Functions

**Q2a)** Returns length of integer numbers

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

**Q2b)** Returns True/False - two strings are same irrespective of lowercase/uppercase

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

**Q2c)** Returns True/False - two strings are anagrams (assume input consists of alphabets only)

```python
>>> str_anagram('god', 'Dog')
True
>>> str_anagram('beat', 'table')
False
>>> str_anagram('beat', 'abet')
True
```

<br>

## <a name="control-structures"></a>3) Control structures

**Q3a)** Write a function that returns

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

**Q3b)** Print all numbers from 1 to 1000 which reads the same in reversed form in both binary and decimal format

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

## <a name="list"></a>4) List

**Q4a)** Write a function that returns product of all numbers of a list

```python
>>> product([1, 4, 21])
84
>>> product([-4, 2.3e12, 77.23, 982, 0b101])
-3.48863356e+18
```

*bonus*: works on any kind of iterable

```python
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

**Q4b)** Write a function that returns nth lowest number of a list (or iterable in general). Return the lowest if second argument not specified

```python
>>> nums = [42, 23421341, 234.2e3, 21, 232, 12312, -2343]
>>> nth_lowest(nums, 3)
42
>>> nth_lowest(nums, 5)
12312
>>> nth_lowest(nums, 15)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in nth_lowest
IndexError: list index out of range

>>> nums = [1, -2, 4, 2, 1, 3, 3, 5]
>>> nth_lowest(nums)
-2
>>> nth_lowest(nums, 4)
2

>>> nth_lowest('unrecognizable', 3)
'c'
```

<br>

## <a name="file"></a>5) File

**Q5a)** Print sum of all numbers from a file containing only single column and all numbers

```
$ cat f1.txt 
8
53
3.14
84
73e2
100
2937

$ ./col_sum.py 
10485.14
```

**Q5b)** Print sum of all numbers (assume only positive integer numbers) from a file containing arbitrary string

```
$ cat f2.txt 
Hello123 World 35
341 2
Good 13day
How are 1784 you

$ ./extract_sum.py 
2298
```

<br>

## <a name="text-processing"></a>6) Text processing

**Q6a)** Check if two words are same or differ by only one character (irrespective of case), input strings should have same length

```python
>>> is_one_char_diff('bar', 'bar')
True
>>> is_one_char_diff('bar', 'Baz')
True
>>> is_one_char_diff('Food', 'fold')
True
>>> is_one_char_diff('A', 'b')
True

>>> is_one_char_diff('a', '')
False
>>> is_one_char_diff('Bar', 'Bark')
False
>>> is_one_char_diff('Bar', 'art')
False
>>> is_one_char_diff('Food', 'fled')
False
>>> is_one_char_diff('ab', '')
False
```

**Q6b)** Check if a word is in ascending/descending alphabetic order or not (irrespective of case)

Can you think of a way to do it only using built-in functions and string methods?

```python
>>> is_alpha_order('bot')
True
>>> is_alpha_order('arT')
True
>>> is_alpha_order('are')
False
>>> is_alpha_order('boat')
False

>>> is_alpha_order('toe')
True
>>> is_alpha_order('Flee')
False
>>> is_alpha_order('reed')
True
```

*bonus*: Check if all words in a sentence (assume only whitespace separated input) are in ascending/descending alphabetic order (irrespective of case)

**hint** use a built-in function and generator expression

```bash
>>> is_alpha_order_sentence('Toe got bit')
True
>>> is_alpha_order_sentence('All is well')
False
```

<br>

## <a name="misc"></a>7) Misc

**Q7a)** Play a song (**hint** use `subprocess` module)

**Q7b)** Open a browser along with any link, for ex: https://github.com/learnbyexample/Python_Basics (**hint** use `webbrowser` module)
