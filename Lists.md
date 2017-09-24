# <a name="lists"></a>Lists

* [Assigning List variables](#assigning-list-variables)
* [Slicing and Modifying Lists](#slicing-and-modifying-lists)
* [Copying Lists](#copying-lists)
* [List Methods and Miscellaneous](#list-methods-and-miscellaneous)
* [Looping](#looping)
* [List Comprehension](#list-comprehension)
* [Getting List as user input](#list-user-input)
* [Getting random items from list](#getting-random-items-from-list)

<br>

### <a name="assigning-list-variables"></a>Assigning List variables

* Simple lists and retrieving list elements

```python
>>> vowels = ['a', 'e', 'i', 'o', 'u']
>>> vowels
['a', 'e', 'i', 'o', 'u']
>>> vowels[0]
'a'
>>> vowels[2]
'i'
>>> vowels[10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

>>> even_numbers = list(range(2, 11, 2))
>>> even_numbers
[2, 4, 6, 8, 10]
>>> even_numbers[-1]
10
>>> even_numbers[-2]
8
>>> even_numbers[-15]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

* Mix of data types and multi-dimensional lists

```python
>>> student = ['learnbyexample', 2016, 'Linux, Vim, Python']
>>> print(student)
['learnbyexample', 2016, 'Linux, Vim, Python']

>>> list_2D = [[1, 3, 2, 10], [1.2, -0.2, 0, 2]]
>>> list_2D[0][0]
1
>>> list_2D[1][0]
1.2
```

* [Python docs - lists](https://docs.python.org/3/tutorial/introduction.html#lists)

<br>

### <a name="slicing-and-modifying-lists"></a>Slicing and Modifying Lists

* Like the `range()` function, list index has `start:stop:step` format, `stop` value being non-inclusive
* [stackoverflow - explain slice notation](https://stackoverflow.com/questions/509211/explain-pythons-slice-notation)

```python
>>> books = ['Harry Potter', 'Sherlock Holmes', 'To Kill a Mocking Bird']
>>> books[2] = "Ender's Game"
>>> print(books)
['Harry Potter', 'Sherlock Holmes', "Ender's Game"]

>>> prime = [2, 3, 5, 7, 11]
>>> prime[2:4]
[5, 7]
>>> prime[:3]
[2, 3, 5]
>>> prime[3:]
[7, 11]

>>> prime[-1]
11
>>> prime[-1:]
[11]
>>> prime[-2:]
[7, 11]


>>> prime[::1]
[2, 3, 5, 7, 11]
>>> prime[::2]
[2, 5, 11]
>>> prime[3:1:-1]
[7, 5]
>>> prime[::-1]
[11, 7, 5, 3, 2]
>>> prime[:]
[2, 3, 5, 7, 11]
```

* when `start` and `stop` values are same
* Useful when they are generated programmatically, see [text processing exercise](./Exercises.md#text-processing) for example

```bash
>>> nums = [1.2, -0.2, 0, 2]
>>> nums[0:0]
[]
>>> nums[2:2]
[]
>>> nums[-1:-1]
[]
>>> nums[21:21]
[]
```

* The indexing format can be used to extract from list variable or modify itself

```python
>>> nums = [1.2, -0.2, 0, 2]
>>> nums[:2] = [1]
>>> nums
[1, 0, 2]

>>> nums = [1.2, -0.2, 0, 2, 4, 23]
>>> nums[:5:2] = [1, 4, 3]
>>> nums
[1, -0.2, 4, 2, 3, 23]

>>> nums = [1, 2, 3, 23]
>>> nums[::-1] = [1, 4, 5, 2]
>>> nums
[2, 5, 4, 1]
```

* helps to modify a list without changing `id`, which is useful if the variable name is referenced elsewhere (see next section)

```python
>>> id(nums)
140598790579336
>>> nums[:] = [1, 2, 5, 4.3]
>>> nums
[1, 2, 5, 4.3]
>>> id(nums)
140598790579336

# assignment without using [:] will change id
>>> nums = [1.2, -0.2, 0, 2]
>>> id(nums)
140598782943752
```

<br>

### <a name="copying-lists"></a>Copying Lists

* Variables in Python contain reference to objects
* For example, when an integer variable is modified, the variable's reference is updated with new object
* the [id()](https://docs.python.org/3/library/functions.html#id) function returns the "identity" of an object
* For variables referring to immutable types like integer and strings, this distinction usually doesn't cause confusion in their usage

```python
>>> a = 5
>>> id(a)
10105952
>>> a = 10
>>> id(a)
10106112

>>> b = a
>>> id(b)
10106112
>>> b = 4
>>> b
4
>>> a
10
>>> id(b)
10105920
```

* But for variables referring to mutable types like lists, it is important to know how variables are copied and passed to functions
* When an element of list variable is modified, it does so by changing the value (mutation) of object at that index

```python
>>> a = [1, 2, 5, 4.3]
>>> a
[1, 2, 5, 4.3]
>>> b = a
>>> b
[1, 2, 5, 4.3]
>>> id(a)
140684757120264
>>> id(b)
140684757120264
>>> b[0] = 'xyz'
>>> b
['xyz', 2, 5, 4.3]
>>> a
['xyz', 2, 5, 4.3]
```

* avoid copying lists using indexing format, it works for 1D lists but not for higher dimensions

```python
>>> prime = [2, 3, 5, 7, 11]
>>> b = prime[:]
>>> id(prime)
140684818101064
>>> id(b)
140684818886024
>>> b[0] = 'a'
>>> b
['a', 3, 5, 7, 11]
>>> prime
[2, 3, 5, 7, 11]

>>> list_2D = [[1, 3, 2, 10], [1.2, -0.2, 0, 2]]
>>> a = list_2D[:]
>>> id(list_2D)
140684818102344
>>> id(a)
140684818103048
>>> a
[[1, 3, 2, 10], [1.2, -0.2, 0, 2]]
>>> a[0][0] = 'a'
>>> a
[['a', 3, 2, 10], [1.2, -0.2, 0, 2]]
>>> list_2D
[['a', 3, 2, 10], [1.2, -0.2, 0, 2]]
```

* use the [copy](https://docs.python.org/3/library/copy.html#module-copy) module instead

```python
>>> import copy
>>> list_2D = [[1, 3, 2, 10], [1.2, -0.2, 0, 2]]
>>> c = copy.deepcopy(list_2D)
>>> c[0][0] = 'a'
>>> c
[['a', 3, 2, 10], [1.2, -0.2, 0, 2]]
>>> list_2D
[[1, 3, 2, 10], [1.2, -0.2, 0, 2]]
```

<br>

### <a name="list-methods-and-miscellaneous"></a>List Methods and Miscellaneous

* adding elements to list

```python
>>> books = []
>>> books
[]
>>> books.append('Harry Potter')
>>> books
['Harry Potter']

>>> even_numbers
[2, 4, 6, 8, 10]
>>> even_numbers += [12, 14, 16, 18, 20]
>>> even_numbers
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

>>> even_numbers = [2, 4, 6, 8, 10]
>>> even_numbers.extend([12, 14, 16, 18, 20])
>>> even_numbers
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

>>> a = [[1, 3], [2, 4]]
>>> a.extend([[5, 6]])
>>> a
[[1, 3], [2, 4], [5, 6]]
```

* deleting elements from a list - based on index

```python
>>> prime = [2, 3, 5, 7, 11]
>>> prime.pop()
11
>>> prime
[2, 3, 5, 7]
>>> prime.pop(0)
2
>>> prime
[3, 5, 7]

>>> list_2D = [[1, 3, 2, 10], [1.2, -0.2, 0, 2]]
>>> list_2D[0].pop(0)
1
>>> list_2D
[[3, 2, 10], [1.2, -0.2, 0, 2]]

>>> list_2D.pop(1)
[1.2, -0.2, 0, 2]
>>> list_2D
[[3, 2, 10]]
```

* using [del](https://docs.python.org/3/reference/simple_stmts.html#del) to delete elements

```python
>>> nums = [1.2, -0.2, 0, 2, 4, 23]
>>> del nums[1]
>>> nums
[1.2, 0, 2, 4, 23]
# can use slicing notation as well
>>> del nums[1:4]
>>> nums
[1.2, 23]

>>> list_2D = [[1, 3, 2, 10], [1.2, -0.2, 0, 2]]
>>> del list_2D[0][1]
>>> list_2D
[[1, 2, 10], [1.2, -0.2, 0, 2]]

>>> del list_2D[0]
>>> list_2D
[[1.2, -0.2, 0, 2]]
```

* clearing list

```python
>>> prime = [2, 3, 5, 7, 11]
>>> prime.clear()
>>> prime
[]
```

* deleting elements from a list - based on value
 
```python
>>> even_numbers = [2, 4, 6, 8, 10]
>>> even_numbers.remove(8)
>>> even_numbers
[2, 4, 6, 10]
>>> even_numbers.remove(12)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```

* inserting elements at a particular index

```python
>>> books = ['Harry Potter', 'Sherlock Holmes', 'To Kill a Mocking Bird']
>>> books.insert(2, "The Martian")
>>> books
['Harry Potter', 'Sherlock Holmes', 'The Martian', 'To Kill a Mocking Bird']
```

* get index of an element

```python
>>> even_numbers = [2, 4, 6, 8, 10]
>>> even_numbers.index(6)
2
>>> even_numbers.index(12)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 12 is not in list
```

* checking if an element is present

```python
>>> prime = [2, 3, 5, 7, 11]
>>> 3 in prime
True
>>> 13 in prime
False
```

* [sorting](https://docs.python.org/3/library/stdtypes.html#list.sort)

```python
>>> a = [1, 5.3, 321, 0, 1, 2]
>>> a.sort()
>>> a
[0, 1, 1, 2, 5.3, 321]

>>> a = [1, 5.3, 321, 0, 1, 2]
>>> a.sort(reverse=True)
>>> a
[321, 5.3, 2, 1, 1, 0]
```

Sort [based on key](https://docs.python.org/3/howto/sorting.html#sortinghowto), for example based on string length  
[lambda expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions) are helpful to pass custom single expression, say sort based on second letter

```python
>>> words = ['fuliginous', 'crusado', 'morello', 'irk', 'seam']
>>> words.sort(key=len)
>>> words
['irk', 'seam', 'crusado', 'morello', 'fuliginous']

>>> words.sort(key=lambda x: x[1])
>>> words
['seam', 'morello', 'irk', 'crusado', 'fuliginous']
```

If original list should not be changed, use [sorted](https://docs.python.org/3/library/functions.html#sorted) function

```python
>>> nums = [-1, 34, 0.2, -4, 309]
>>> nums_desc = sorted(nums, reverse=True)
>>> nums_desc
[309, 34, 0.2, -1, -4]

>>> sorted(nums, key=abs)
[0.2, -1, -4, 34, 309]
```

* `min` and `max`

```python
>>> a = [321, 899.232, 5.3, 2, 1, -1]
>>> min(a)
-1
>>> max(a)
899.232
```

* Number of times an item is present

```python
>>> nums = [15, 99, 19, 382, 43, 19]
>>> nums.count(99)
1
>>> nums.count(19)
2
>>> nums.count(23)
0
```

* reverse list in place

```python
>>> prime = [2, 3, 5, 7, 11]
>>> id(prime)
140684818102088
>>> prime.reverse()
>>> prime
[11, 7, 5, 3, 2]
>>> id(prime)
140684818102088

>>> a = [1, 5.3, 321, 0, 1, 2]
>>> id(a)
140684818886024
>>> a = a[::-1]
>>> a
[2, 1, 0, 321, 5.3, 1]
>>> id(a)
140684818102664
```

* [len](https://docs.python.org/3/library/functions.html#len) function to get size of lists

```python
>>> prime
[2, 3, 5, 7, 11]
>>> len(prime)
5

>>> s = len(prime) // 2
>>> prime[:s]
[2, 3]
>>> prime[s:]
[5, 7, 11]
```

* summing numeric lists

```python
>>> a
[321, 5.3, 2, 1, 1, 0]
>>> sum(a)
330.3
```

* [all](https://docs.python.org/3/library/functions.html#all) and [any](https://docs.python.org/3/library/functions.html#any) functions

```python
>>> conditions = [True, False, True]
>>> all(conditions)
False
>>> any(conditions)
True

>>> conditions[1] = True
>>> all(conditions)
True

>>> a = [321, 5.3, 2, 1, 1, 0]
>>> all(a)
False
>>> any(a)
True
```

* comparing lists

```python
>>> prime
[2, 3, 5, 7, 11]
>>> a = [4, 2]
>>> prime == a
False

>>> prime == [2, 3, 5, 11, 7]
False
>>> prime == [2, 3, 5, 7, 11]
True
```

**Further Reading**

* [Python docs - more on lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
* [Python docs - collections](https://docs.python.org/3/library/collections.html)

<br>

### <a name="looping"></a>Looping

```python
#!/usr/bin/python3

numbers = [2, 12, 3, 25, 624, 21, 5, 9, 12]
odd_numbers  = []
even_numbers = []

for num in numbers:
    odd_numbers.append(num) if(num % 2) else even_numbers.append(num)

print("numbers:      {}".format(numbers))
print("odd_numbers:  {}".format(odd_numbers))
print("even_numbers: {}".format(even_numbers))
```

* usually, it is enough to deal with every element of list without needing index of elements

```
$ ./list_looping.py 
numbers:      [2, 12, 3, 25, 624, 21, 5, 9, 12]
odd_numbers:  [3, 25, 21, 5, 9]
even_numbers: [2, 12, 624, 12]
```

* use `enumerate()` if both index and element is needed

```python
#!/usr/bin/python3

north_dishes = ['Aloo tikki', 'Baati', 'Khichdi', 'Makki roti', 'Poha']

print("My favorite North Indian dishes:")
for idx, item in enumerate(north_dishes):
    print("{}. {}".format(idx + 1, item))
```

* In this case, we get a [tuple](./Sequence_Set_Dict_data_types.md#tuples) every iteration consisting of a count (default value 0) and an item from the list
* [Python docs - enumerate](https://docs.python.org/3/library/functions.html#enumerate)

```
$ ./list_looping_enumeration.py
My favorite North Indian dishes:
1. Aloo tikki
2. Baati
3. Khichdi
4. Makki roti
5. Poha
```

* a start value can also be specified

```python
>>> north_dishes = ['Aloo tikki', 'Baati', 'Khichdi', 'Makki roti', 'Poha']
>>> for idx, item in enumerate(north_dishes, start=1):
...     print(idx, item, sep='. ')
... 
1. Aloo tikki
2. Baati
3. Khichdi
4. Makki roti
5. Poha
```

* use `zip()` to iterate over two or more lists simultaneously
* [Python docs - zip](https://docs.python.org/3/library/functions.html#zip)

```python
>>> odd = [1, 3, 5]
>>> even = [2, 4, 6]
>>> for i, j in zip(odd, even):
...     print(i + j)
... 
3
7
11
```

<br>

### <a name="list-comprehension"></a>List Comprehension

```python
#!/usr/bin/python3

import time

numbers = list(range(1,100001))
fl_square_numbers = []

# reference time
t0 = time.perf_counter()

# ------------ for loop ------------
for num in numbers:
    fl_square_numbers.append(num * num)

# reference time
t1 = time.perf_counter()

# ------- list comprehension -------
lc_square_numbers = [num * num for num in numbers]

# performance results
t2 = time.perf_counter()
fl_time = t1 - t0
lc_time = t2 - t1
improvement = (fl_time - lc_time) / fl_time * 100

print("Time with for loop:           {:.4f}".format(fl_time))
print("Time with list comprehension: {:.4f}".format(lc_time))
print("Improvement:                  {:.2f}%".format(improvement))

if fl_square_numbers == lc_square_numbers:
    print("\nfl_square_numbers and lc_square_numbers are equivalent")
else:
    print("\nfl_square_numbers and lc_square_numbers are NOT equivalent")
```

* List comprehensions is a Pythonic way for some of the common looping constructs
* Usually is a more readable and time saving option than loops
* In this example, not having to call `append()` method also saves lot of time in case of list comprehension
* Time values in this example is indicative and not to be taken as absolute
    * It usually varies even between two runs, let alone different machines

```
$ ./list_comprehension.py
Time with for loop:           0.0142
Time with list comprehension: 0.0062
Improvement:                  56.36%

fl_square_numbers and lc_square_numbers are equivalent
```

* conditional list comprehension

```python
# using if-else conditional in list comprehension
numbers = [2, 12, 3, 25, 624, 21, 5, 9, 12]
odd_numbers  = []
even_numbers = []
[odd_numbers.append(num) if(num % 2) else even_numbers.append(num) for num in numbers]

# or a more simpler and readable approach
numbers = [2, 12, 3, 25, 624, 21, 5, 9, 12]
odd_numbers  = [num for num in numbers if num % 2]
even_numbers = [num for num in numbers if not num % 2]
```

* zip example

```python
>>> p = [1, 3, 5]
>>> q = [3, 214, 53]
>>> [i+j for i,j in zip(p, q)]
[4, 217, 58]
>>> [i*j for i,j in zip(p, q)]
[3, 642, 265]
```

use [generator expressions](https://docs.python.org/3/tutorial/classes.html#generator-expressions) if sequence needs to be passed onto another function

```python
>>> sum(i*j for i,j in zip(p, q))
910
```

**Further Reading**

For more examples, including nested loops, check these

* [Python docs - list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
* [Python List Comprehensions: Explained Visually](http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/)
* [are list comprehensions and functional functions faster than for loops](http://stackoverflow.com/questions/22108488/are-list-comprehensions-and-functional-functions-faster-than-for-loops)
* [Python docs - perf_counter](https://docs.python.org/3/library/time.html#time.perf_counter)
    * [understanding perf_counter and process_time](http://stackoverflow.com/questions/25785243/understanding-time-perf-counter-and-time-process-time)
* [Python docs - timeit](https://docs.python.org/3/library/timeit.html)

<br>

### <a name="list-user-input"></a>Getting List as user input

```python
>>> b = input('Enter strings separated by space: ').split()
Enter strings separated by space: foo bar baz
>>> b
['foo', 'bar', 'baz']

>>> nums = [int(n) for n in input('Enter numbers separated by space: ').split()]
Enter numbers separated by space: 1 23 5
>>> nums
[1, 23, 5]

>>> ip_str = input('Enter prime numbers separated by comma: ')
Enter prime numbers separated by comma: 3,5,7
>>> primes = [int(n) for n in ip_str.split(',')]
>>> primes
[3, 5, 7]
```

* Since user input is all treated as string, need to process based on agreed delimiter and required data type

<br>

### <a name="getting-random-items-from-list"></a>Getting random items from list

* Get a random item

```python
>>> import random
>>> a = [4, 5, 2, 76]
>>> random.choice(a)
76
>>> random.choice(a)
4
```

* Randomly re-arrange items of list

```python
>>> random.shuffle(a)
>>> a
[5, 2, 76, 4]
```

* Get random slice of list, doesn't modify the list variable

```python
>>> random.sample(a, k=3)
[76, 2, 5]

>>> random.sample(range(1000), k=5)
[68, 203, 15, 757, 580]
```

* Get random items from list without repetition by creating an iterable using [Python docs - iter](https://docs.python.org/3/library/functions.html#iter) function 
* The difference from simply using shuffled list is that this avoids the need to maintain a separate index counter and automatic exception raised if it goes out of range

```python
>>> nums = [1, 3, 6, -12, 1.2, 3.14]
>>> random.shuffle(nums)
>>> nums_iter = iter(nums)
>>> print(next(nums_iter))
3.14
>>> print(next(nums_iter))
1.2
>>> for n in nums_iter:
...     print(n)
... 
1
3
-12
6
>>> print(next(nums_iter))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

* [Python docs - random](https://docs.python.org/3/library/random.html) for more info
  * new in version 3.6 - [random.choices](https://docs.python.org/3/library/random.html#random.choices)
* [Python docs - next](https://docs.python.org/3/library/functions.html#next)
* See also [yield](https://stackoverflow.com/questions/231767/what-is-the-function-of-the-yield-keyword)
