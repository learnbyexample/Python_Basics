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

# bonus
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
* Print all numbers from 1 to 1000 which reads the same in reversed form in both binary and decimal format
    * For example, `313` whose binary is `100111001`

<br>

## <a name="list"></a>List

* Write a function that returns product of all numbers of a list
* Write a function that returns 3rd lowest number of a list
	* input list can contain duplicate numbers as well

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

