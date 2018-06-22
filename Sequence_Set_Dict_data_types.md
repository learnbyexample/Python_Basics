# <a name="sequence-data-types"></a>Sequence, Set and Dict data types

* [Strings](#strings)
* [Tuples](#tuples)
* [Set](#set)
* [Dictionary](#dictionary)

We have already seen Sequence types in previous chapters - strings, ranges and lists. Tuple is another sequence type  
We'll see some more operations on strings followed by Tuple, Set and Dict in this chapter

<br>

### <a name="strings"></a>Strings

* The indexing we saw for lists can be applied to strings as well
    * As strings are immutable, they can't be modified like lists though

```python
>>> book = "Alchemist"
>>> book[0]
'A'
>>> book[3]
'h'
>>> book[-1]
't'
>>> book[10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range

>>> book[2:6]
'chem'
>>> book[:5]
'Alche'
>>> book[5:]
'mist'
>>> book[::-1]
'tsimehclA'
>>> book[:]
'Alchemist'

>>> list(book)
['A', 'l', 'c', 'h', 'e', 'm', 'i', 's', 't']

>>> import string
>>> string.ascii_lowercase[:10]
'abcdefghij'
>>> list(string.digits)
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```

* looping over strings

```python
>>> book
'Alchemist'

>>> for char in book:
...     print(char)
... 
A
l
c
h
e
m
i
s
t
```

* Other operations

```python
>>> book
'Alchemist'

>>> len(book)
9

>>> book.index('A')
0
>>> book.index('t')
8

>>> 'A' in book
True
>>> 'B' in book
False
>>> 'z' not in book
True

>>> min('zealous')
'a'
>>> max('zealous')
'z'
```

<br>

### <a name="tuples"></a>Tuples

* Tuples are similar to lists but immutable and useful in other ways too
* Individual elements can be both mutable/immutable

```python
>>> north_dishes = ('Aloo tikki', 'Baati', 'Khichdi', 'Makki roti', 'Poha')
>>> north_dishes
('Aloo tikki', 'Baati', 'Khichdi', 'Makki roti', 'Poha')

>>> north_dishes[0]
'Aloo tikki'
>>> north_dishes[-1]
'Poha'
>>> north_dishes[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range

>>> north_dishes[::-1]
('Poha', 'Makki roti', 'Khichdi', 'Baati', 'Aloo tikki')

>>> north_dishes[0] = 'Poori'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

* Example operations

```python
>>> 'roti' in north_dishes
False
>>> 'Makki roti' in north_dishes
True

>>> len(north_dishes)
5

>>> min(north_dishes)
'Aloo tikki'
>>> max(north_dishes)
'Poha'

>>> for dish in north_dishes:
...     print(dish)
... 
Aloo tikki
Baati
Khichdi
Makki roti
Poha
```

* Tuple is handy for multiple variable assignment and returning more than one value in functions
    * We have already seen example when using `enumerate` for iterating over lists

```python
>>> a = 5
>>> b = 20
>>> a, b = b, a
>>> a
20
>>> b
5

>>> c = 'foo'
>>> a, b, c = c, a, b
>>> a
'foo'
>>> b
20
>>> c
5

>>> def min_max(arr):
...     return min(arr), max(arr)
... 
>>> min_max([23, 53, 1, -34, 9])
(-34, 53)
```

* using `()` is not always required

```python
>>> words = 'day', 'night'
>>> words
('day', 'night')

>>> coordinates = ((1,2), (4,3), (92,3))
>>> coordinates
((1, 2), (4, 3), (92, 3))

>>> prime = [2, 3, 5, 7, 11]
>>> prime_tuple = tuple((idx + 1, num) for idx, num in enumerate(prime))
>>> prime_tuple
((1, 2), (2, 3), (3, 5), (4, 7), (5, 11))
```

* converting other types to tuples
    * similar to `list()`

```
>>> tuple('books')
('b', 'o', 'o', 'k', 's')

>>> a = [321, 899.232, 5.3, 2, 1, -1]
>>> tuple(a)
(321, 899.232, 5.3, 2, 1, -1)
```

* data types can be mixed and matched in different ways

```python
>>> a = [(1,2), ['a', 'b'], ('good', 'bad')]
>>> a
[(1, 2), ['a', 'b'], ('good', 'bad')]

>>> b = ((1,2), ['a', 'b'], ('good', 'bad'))
>>> b
((1, 2), ['a', 'b'], ('good', 'bad'))
```

* [Python docs - tuple](https://docs.python.org/3/library/stdtypes.html#tuple)
* [Python docs - tuple tutorial](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

<br>

### <a name="set"></a>Set

* Set is unordered collection of objects
* Mutable data type
* Typically used to maintain unique sequence, perform Set operations like intersection, union, difference, symmetric difference, etc

```python
>>> nums = {3, 2, 5, 7, 1, 6.3}
>>> nums
{1, 2, 3, 5, 6.3, 7}

>>> primes = {3, 2, 11, 3, 5, 13, 2}
>>> primes
{2, 3, 11, 13, 5}

>>> nums.union(primes)
{1, 2, 3, 5, 6.3, 7, 11, 13}

>>> primes.difference(nums)
{11, 13}
>>> nums.difference(primes)
{1, 6.3, 7}
```

* Example operations

```python
>>> len(nums)
6

>>> nums[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing

>>> book
'Alchemist'
>>> set(book)
{'i', 'l', 's', 'A', 'e', 'h', 'm', 't', 'c'}
>>> set([1, 5, 3, 1, 9])
{1, 9, 3, 5}
>>> list(set([1, 5, 3, 1, 9]))
[1, 9, 3, 5]

>>> nums = {1, 2, 3, 5, 6.3, 7}
>>> nums
{1, 2, 3, 5, 6.3, 7}
>>> nums.pop()
1
>>> nums
{2, 3, 5, 6.3, 7}

>>> nums.add(1)
>>> nums
{1, 2, 3, 5, 6.3, 7}

>>> 6.3 in nums
True

>>> for n in nums:
...     print(n)
... 
1
2
3
5
6.3
7
```

* [Python docs - set](https://docs.python.org/3/library/stdtypes.html#set)
* [Python docs - frozenset](https://docs.python.org/3/library/stdtypes.html#frozenset)
* [set tutorial](http://www.programiz.com/python-programming/set)

<br>

### <a name="dictionary"></a>Dictionary

* `dict` types can be thought of as unordered list of `key:value` pairs or a named list of items
* up to Python v3.5 (and some implementations of v3.6) do not retain order of insertion of dict elements

```python
>>> marks = {'Rahul' : 86, 'Ravi' : 92, 'Rohit' : 75}
>>> marks
{'Ravi': 92, 'Rohit': 75, 'Rahul': 86}

>>> fav_books = {}
>>> fav_books['fantasy']   = 'Harry Potter'
>>> fav_books['detective'] = 'Sherlock Holmes'
>>> fav_books['thriller']  = 'The Da Vinci Code'
>>> fav_books
{'thriller': 'The Da Vinci Code', 'fantasy': 'Harry Potter', 'detective': 'Sherlock Holmes'}

>>> marks.keys()
dict_keys(['Ravi', 'Rohit', 'Rahul'])

>>> fav_books.values()
dict_values(['The Da Vinci Code', 'Harry Potter', 'Sherlock Holmes'])
```

* looping and printing

```python
>>> for book in fav_books.values():
...     print(book)
... 
The Da Vinci Code
Harry Potter
Sherlock Holmes

>>> for name, mark in marks.items():
...     print(name, mark, sep=': ')
... 
Ravi: 92
Rohit: 75
Rahul: 86

>>> import pprint
>>> pp = pprint.PrettyPrinter(indent=4)
>>> pp.pprint(fav_books)
{   'detective': 'Sherlock Holmes',
    'fantasy': 'Harry Potter',
    'thriller': 'The Da Vinci Code'}
```

* modifying dicts and example operations

```python
>>> marks
{'Ravi': 92, 'Rohit': 75, 'Rahul': 86}
>>> marks['Rajan'] = 79
>>> marks
{'Ravi': 92, 'Rohit': 75, 'Rahul': 86, 'Rajan': 79}

>>> del marks['Ravi']
>>> marks
{'Rohit': 75, 'Rahul': 86, 'Rajan': 79}

>>> len(marks)
3

>>> fav_books
{'thriller': 'The Da Vinci Code', 'fantasy': 'Harry Potter', 'detective': 'Sherlock Holmes'}
>>> "fantasy" in fav_books
True
>>> "satire" in fav_books
False
```

* dict made up of lists and using random module
* any change in the individual lists will also reflect in dict
* output of `keys()` method has to be changed to Sequence types like `list` or `tuple` to pass on to `random.choice`

```python
>>> north = ['aloo tikki', 'baati', 'khichdi', 'makki roti', 'poha']
>>> south = ['appam', 'bisibele bath', 'dosa', 'koottu', 'sevai']
>>> west = ['dhokla', 'khakhra', 'modak', 'shiro', 'vada pav']
>>> east = ['hando guri', 'litti', 'momo', 'rosgulla', 'shondesh']
>>> dishes = {'North': north, 'South': south, 'West': west, 'East': east}

>>> rand_zone = random.choice(tuple(dishes.keys()))
>>> rand_dish = random.choice(dishes[rand_zone])
>>> print("Try the '{}' speciality '{}' today".format(rand_zone, rand_dish))
Try the 'East' speciality 'rosgulla' today
```

* From Python v3.7 onwards, dict implementation will retain insertion order
    * some implementations like the reference CPython implementation for v3.6 also retains the insertion order

```python
>>> marks = {'Rahul' : 86, 'Ravi' : 92, 'Rohit' : 75, 'Rajan': 79}
>>> marks
{'Rahul': 86, 'Ravi': 92, 'Rohit': 75, 'Rajan': 79}

>>> for name, mark in marks.items():
...     print(f'{name:5s}: {mark}')
... 
Rahul: 86
Ravi : 92
Rohit: 75
Rajan: 79

>>> del marks['Ravi']
>>> marks
{'Rahul': 86, 'Rohit': 75, 'Rajan': 79}

>>> marks['Ranjit'] = 65
>>> marks
{'Rahul': 86, 'Rohit': 75, 'Rajan': 79, 'Ranjit': 65}
```

**Further Reading**

* [Python docs - dict](https://docs.python.org/3/library/stdtypes.html#dict)
* [Python docs - pprint](https://docs.python.org/3/library/pprint.html)
* [detailed tutorial on dict](http://www.sharats.me/posts/the-python-dictionary/)
* [Using dict to eliminate duplicates while retaining order](https://twitter.com/raymondh/status/944125570534621185)

