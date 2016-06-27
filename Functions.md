# <a name="functions"></a>Functions

* [def](#def)
* [print function](#print-function)
* [range function](#range-function)
* [type function](#type-function)
* [Variable Scope](#variable-scope)

<br>
### <a name="def"></a>def

```python
#!/usr/bin/python3

# ----- function without arguments -----
def greeting():
    print("-----------------------------")
    print("         Hello World         ")
    print("-----------------------------")

greeting()

# ----- function with arguments -----
def sum_two_numbers(num1, num2):
    sum = num1 + num2
    print("{} + {} = {}".format(num1, num2, sum))

sum_two_numbers(3, 4)

# ----- function with return value -----
def num_square(num):
    return num * num

my_num = 3
print(num_square(2))
print(num_square(my_num))
```

* The `def` keyword is used to define functions
* Functions have to be defined before use
* A common syntax error is leaving out `:` at end of `def` statement
* Block of code for functions, control structures, etc are distinguished by indented code
    * 4-space indentation is recommended
    * [Python docs - Coding Style](https://docs.python.org/3/tutorial/controlflow.html#intermezzo-coding-style)
* The default `return` value is `None`
* [How variables are passed to functions in Python](http://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/)

```
$ ./functions.py 
-----------------------------
         Hello World         
-----------------------------
3 + 4 = 7
4
9
```

**Default valued arguments**

```python
#!/usr/bin/python3

# ----- function with default valued argument -----
def greeting(style_char='-'):
    print(style_char * 29)
    print("         Hello World         ")
    print(style_char * 29)

print("Default style")
greeting()

print("\nStyle character *")
greeting('*')

print("\nStyle character =")
greeting(style_char='=')
```

* Often, functions can have a default behavior and if needed changed by passing relevant argument

```
$ ./functions_default_arg_value.py 
Default style
-----------------------------
         Hello World         
-----------------------------

Style character *
*****************************
         Hello World         
*****************************

Style character =
=============================
         Hello World         
=============================
```

**Further Reading**

There are many more ways to call a function and other types of declarations, refer the below links for more info

* [Python docs - defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
* [Python docs - Built-in Functions](https://docs.python.org/3/library/functions.html)

<br>
### <a name="print-function"></a>print function

* By default, `print` function adds newline character
* This can be changed by passing our own string to the `end` argument

```python
>>> print("hi")
hi
>>> print("hi", end='')
hi>>> 
>>> print("hi", end=' !!\n')
hi !!
>>> 
```

* Printing variables - requires explicit type conversion to `str` for numeric variables when used for string concatenation

```python
>>> greeting = 'Hello World'
>>> print(greeting)
Hello World
>>> num = 42
>>> print(num)
42

>>> print(greeting + '. We are learning Python')
Hello World. We are learning Python

>>> print("The Ultimate Answer to Life, The Universe and Everything is..." + num)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly

>>> print("The Ultimate Answer to Life, The Universe and Everything is..." + str(num))
The Ultimate Answer to Life, The Universe and Everything is...42
```

* `str.format()` can be used to style strings and handle multiple variables more elegantly than string concatenation

```python
>>> num1 = 42
>>> num2 = 7
>>> print("{} + {} = {}".format(num1, num2, num1 + num2))
42 + 7 = 49
```

* using numbered arguments

```python
>>> num1
42
>>> num2
7
>>> print("{0} + {1} * {0} = {2}".format(num1, num2, num1 + num2 * num1))
42 + 7 * 42 = 336
```

* number formatting - specified using optional argument number, followed by `:` and then the formatting style

```python
>>> appx_pi = 22 / 7
>>> appx_pi
3.142857142857143
>>> print("{0:.2f}".format(appx_pi))
3.14
>>> print("{0:10.3f}".format(appx_pi))
     3.143
```

* different base

```python
>>> num1
42
>>> print("42 in binary = {:b}".format(num1))
42 in binary = 101010
>>> print("42 in octal = {:o}".format(num1))
42 in octal = 52
>>> print("42 in hex = {:x}".format(num1))
42 in hex = 2a

>>> hex_str = "{:x}".format(num1)
>>> hex_str
'2a'
>>> int(hex_str, 16)
42
```

* [Python docs - formatstrings](https://docs.python.org/3/library/string.html#formatstrings) - for more info and examples

<br>
### <a name="range-function"></a>range function

* By default `start=0` and `step=1`, so they can be skipped or defined as appropriate
    * `range(stop)`
    * `range(start, stop)`
    * `range(start, stop, step)`
* Note that `range` output doesn't include `stop` value - it is always upto `stop` value but not including it
* We'll see more about `list` function and data type in later chapters

```python
>>> range(5)
range(0, 5)

>>> list(range(5))
[0, 1, 2, 3, 4]

>>> list(range(-2, 2))
[-2, -1, 0, 1]

>>> list(range(1, 15, 2))
[1, 3, 5, 7, 9, 11, 13]

>>> list(range(10, -5, -2))
[10, 8, 6, 4, 2, 0, -2, -4]
```

* [Python docs - Ranges](https://docs.python.org/3/library/stdtypes.html#typesseq-range) - for more info and examples

<br>
### <a name="type-function"></a>type function

Useful to check data type of a variable or value

```python
>>> type(5)
<class 'int'>

>>> type('Hi there!')
<class 'str'>

>>> type(range(7))
<class 'range'>

>>> type(None)
<class 'NoneType'>

>>> type(True)
<class 'bool'>

>>> arr = list(range(4))
>>> arr
[0, 1, 2, 3]
>>> type(arr)
<class 'list'>
```

<br>
### <a name="variable-scope"></a>Variable Scope

```python
#!/usr/bin/python3

def print_num():
    print("Yeehaw! num is visible in this scope, its value is: " + str(num))

num = 25
print_num()
```

* Variables defined before function call are visible within the function scope too 
* [Python docs - Default Argument Values](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values) - see description for when default values are evaluated

```
$ ./variable_scope_1.py 
Yeehaw! num is visible in this scope, its value is: 25
```

What happens when a variable declared within a block is used outside of it?

```python
#!/usr/bin/python3

def square_of_num(num):
    sqr_num = num * num

square_of_num(5)
print("5 * 5 = {}".format(sqr_num))
```

* Here, `sqr_num` is declared inside `square_of_num` function and not accessible outside the block

```
$ ./variable_scope_2.py 
Traceback (most recent call last):
  File "./variable_scope_2.py", line 7, in <module>
    print("5 * 5 = {}".format(sqr_num))
NameError: name 'sqr_num' is not defined
```

One way to overcome this is to use the `global` keyword

```python
#!/usr/bin/python3

def square_of_num(num):
    global sqr_num
    sqr_num = num * num

square_of_num(5)
print("5 * 5 = {}".format(sqr_num))
```

* Now, we can access `sqr_num` even outside the function definition

```
$ ./variable_scope_3.py
5 * 5 = 25
```

If a variable name is same outside and within function definition, the one inside the function will stay local to the block and not affect the one outside of it

```python
#!/usr/bin/python3

sqr_num = 4

def square_of_num(num):
    sqr_num = num * num
    print("5 * 5 = {}".format(sqr_num))

square_of_num(5)
print("Whoops! sqr_num is still {}!".format(sqr_num))
```

* Note that using `global sqr_num` will affect the `sqr_num` variable outside the function

```
$ ./variable_scope_4.py 
5 * 5 = 25
Whoops! sqr_num is still 4!
```

**Further Reading**

* [Python docs - scope example](https://docs.python.org/3/tutorial/classes.html#scopes-and-namespaces-example)
* [Python docs - global statement](https://docs.python.org/3/reference/simple_stmts.html#the-global-statement)
