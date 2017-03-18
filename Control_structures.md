# <a name="control-structures"></a>Control Structures

* [Condition checking](#condition-checking)
* [if](#if)
* [for](#for)
* [while](#while)
* [continue and break](#continue-and-break)

<br>

### <a name="condition-checking"></a>Condition checking

* simple and combination of tests

```python
>>> num = 5
>>> num > 2
True
>>> num > 3 and num <= 5
True
>>> 3 < num <= 5
True
>>> num % 3 == 0 or num % 5 == 0
True

>>> fav_fiction = 'Harry Potter'
>>> fav_detective = 'Sherlock Holmes'
>>> fav_fiction == fav_detective
False
>>> fav_fiction == "Harry Potter"
True
```

* Testing variable or value by themselves

```python
>>> bool(num)
True
>>> bool(fav_detective)
True
>>> bool(3)
True
>>> bool(0)
False
>>> bool("")
False
>>> bool(None)
False

>>> if -1:
...     print("-1 evaluates to True in condition checking")
... 
-1 evaluates to True in condition checking
```

* The use of `in` operator in condition checking

Compare this way of checking

```python
>>> def num_chk(n):
...     if n == 10 or n == 21 or n == 33:
...         print("Number passes condition")
...     else:
...         print("Number fails condition")
... 
>>> num_chk(10)
Number passes condition
>>> num_chk(12)
Number fails condition
```

vs this one

```python
>>> def num_chk(n):
...     if n in (10, 21, 33):
...         print("Number passes condition")
...     else:
...         print("Number fails condition")
... 
>>> num_chk(12)
Number fails condition
>>> num_chk(10)
Number passes condition
```

* `(10, 21, 33)` is a tuple data type, will be covered in later chapters
* [Python docs - Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth)

<br>

### <a name="if"></a>if

```python
#!/usr/bin/python3

num = 45

# only if
if num > 25:
    print("Hurray! {} is greater than 25".format(num))

# if-else
if num % 2 == 0:
    print("{} is an even number".format(num))
else:
    print("{} is an odd number".format(num))

# if-elif-else
# any number of elif can be used
if num < 0:
    print("{} is a negative number".format(num))
elif num > 0:
    print("{} is a positive number".format(num))
else:
    print("{} is neither postive nor a negative number".format(num))
```

* Block of code for functions, control structures, etc are distinguished by indented code
    * 4-space indentation is recommended
    * [Python docs - Coding Style](https://docs.python.org/3/tutorial/controlflow.html#intermezzo-coding-style)
* A common syntax error is leaving out `:` at end of control structure statements
* Using `()` around conditions is optional
* indented block can have any number of statements, including blank lines

```
$ ./if_elif_else.py 
Hurray! 45 is greater than 25
45 is an odd number
45 is a positive number
```

**if-else** as conditional operator

```python
#!/usr/bin/python3

num = 42

num_type = 'even' if num % 2 == 0 else 'odd'
print("{} is an {} number".format(num, num_type))
```

* Python doesn't have `?:` conditional operator like many other languages
* Using `if-else` in single line like in this example is one workaround
* [More ways of simulating ternary conditional operator](http://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator)

```
$ ./if_else_oneliner.py 
42 is an even number
```

<br>

### <a name="for"></a>for

```python
#!/usr/bin/python3

number = 9
for i in range(1, 5):
    mul_table = number * i
    print("{} * {} = {}".format(number, i, mul_table))
```

* traditional iteration based loop can be written using `range` function
    * recall that by default `start=0`, `step=1` and `stop` value is not inclusive
* iterating over variables like list, tuples, etc will be covered in later chapters
* [Python docs - itertools](https://docs.python.org/3/library/itertools.html)

```
$ ./for_loop.py 
9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
```

<br>

### <a name="while"></a>while

```python
#!/usr/bin/python3

# continuously ask user input till it is a positive integer
usr_string = 'not a number'
while not usr_string.isnumeric():
    usr_string = input("Enter a positive integer: ")
```

* while loop allows us to execute block of statements until a condition is satisfied
* [Python docs - string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

```
$ ./while_loop.py 
Enter a positive integer: abc
Enter a positive integer: 1.2
Enter a positive integer: 23
$ 
```

<br>

### <a name="continue-and-break"></a>continue and break

The `continue` and `break` keywords are used to change the normal flow of loops on certain conditions

**continue** - skip rest of statements in the loop and start next iteration

```python
#!/usr/bin/python3

prev_num = 0
curr_num = 0
print("The first ten numbers in fibonacci sequence: ", end='')

for num in range(10):
    print(curr_num, end=' ')

    if num == 0:
        curr_num = 1
        continue

    temp = curr_num
    curr_num = curr_num + prev_num
    prev_num = temp

print("")
```

* `continue` can be placed anywhere in a loop block without having to worry about complicated code flow
* this example is just to show use of `continue`, check [this](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) for a more Pythonic way

```
$ ./loop_with_continue.py 
The first ten numbers in fibonacci sequence: 0 1 1 2 3 5 8 13 21 34
```

**break** - skip rest of statements in the loop (if any) and exit loop

```python
#!/usr/bin/python3

import random

while True:
    # as with range() function, 500 is not inclusive
    random_int = random.randrange(500)
    if random_int % 4 == 0 and random_int % 6 == 0:
        break
print("Random number divisible by 4 and 6: {}".format(random_int))
```

* `while True:` is generally used as infinite loop
* **randrange** has similar `start, stop, step` arguments as [range](./Functions.md#range-function)
* [Python docs - random](https://docs.python.org/3/library/random.html)

```
$ ./loop_with_break.py 
Random number divisible by 4 and 6: 168
$ ./loop_with_break.py 
Random number divisible by 4 and 6: 216
$ ./loop_with_break.py 
Random number divisible by 4 and 6: 24
```

The while_loop.py example can be re-written using `break`

```python
>>> while True:
         usr_string = input("Enter a positive integer: ")
         if usr_string.isnumeric():
             break
    
Enter a positive integer: a
Enter a positive integer: 3.14
Enter a positive integer: 1
>>>
```

* in case of nested loops, `continue` and `break` only affect the immediate parent loop
* [Python docs - else clauses on loops](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
