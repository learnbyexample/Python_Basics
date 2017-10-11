# <a name="exception-handling-and-debugging"></a>Exception Handling and Debugging

* [Exception Handling](#exception-handling)
* [Syntax check](#syntax-check)
* [pdb](#pdb)
* [Importing program](#importing-program)

<br>

### <a name="exception-handling"></a>Exception Handling

* We have seen plenty of errors in previous chapters when something goes wrong or some input was given erroneously
* For example:

```
$ ./user_input_int.py 
Enter an integer number: abc
Traceback (most recent call last):
  File "./user_input_int.py", line 6, in <module>
    usr_num = int(usr_ip)
ValueError: invalid literal for int() with base 10: 'abc'
```

* In such cases, it might be preferred to inform the user on the error and give a chance to correct it
* Python provides the `try-except` construct to achieve this

```python
#!/usr/bin/python3

while True:
    try:
        usr_num = int(input("Enter an integer number: "))
        break
    except ValueError:
        print("Not an integer, try again")

print("Square of entered number is: {}".format(usr_num * usr_num))
```

* `except` can be used for particular error (in this case `ValueError`)

```
$ ./user_input_exception.py
Enter an integer number: a
Not an integer, try again
Enter an integer number: 1.2
Not an integer, try again
Enter an integer number: 3
Square of entered number is: 9
```

**Further Reading**

* [Python docs - errors, exception handling and raising exceptions](https://docs.python.org/3/tutorial/errors.html)
* [Python docs - built-in exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)
* [stackoverflow - exception message capturing](https://stackoverflow.com/questions/4690600/python-exception-message-capturing)
* [stackoverflow - avoid bare exceptions](https://stackoverflow.com/questions/14797375/should-i-always-specify-an-exception-type-in-except-statements)
* [Python docs - pass statement](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-pass_stmt)

<br>

### <a name="syntax-check"></a>Syntax check

* Python's command line options can be used for variety of purposes
* Syntax checking is one of them

```
$ python3 -m py_compile syntax_error.py 
  File "syntax_error.py", line 3
    print "Have a nice day"
                          ^
SyntaxError: Missing parentheses in call to 'print'
```

* Useful to quickly catch syntax errors like missing `:` for `if for with` etc and `()` for `print` statements
* While this example might be trivial, real world program might have thousands of lines and tougher to find typos
* [Python docs - cmdline](https://docs.python.org/3/using/cmdline.html)
    * One-liners: [#1](http://www.vurt.ru/2013/02/python-command-line-oneliners/), [#2](https://wiki.python.org/moin/Powerful%20Python%20One-Liners), [#3](http://python-oneliner.readthedocs.org/en/latest/)

<br>

### <a name="pdb"></a>pdb

* Invoking debugger is another use of `cmdline`
* Use it instead of using `print` all over a program when something goes wrong, plus one can use breakpoints and other features specific to debugging programs

```python
$ python3 -m pdb if_elif_else.py 
> /home/learnbyexample/python_programs/if_elif_else.py(3)<module>()
-> num = 45
(Pdb) p num
*** NameError: name 'num' is not defined
(Pdb) n
> /home/learnbyexample/python_programs/if_elif_else.py(6)<module>()
-> if num > 25:
(Pdb) p num
45
(Pdb) l
  1  	#!/usr/bin/python3
  2  	
  3  	num = 45
  4  	
  5  	# only if
  6  ->	if num > 25:
  7  	    print("Hurray! {} is greater than 25".format(num))
  8  	
  9  	# if-else
 10  	if num % 2 == 0:
 11  	    print("{} is an even number".format(num))
(Pdb) q
```

* `l` prints code around the current statement the debugger is at, useful to visualize the progress of debug effort
* `s` execute current line, steps inside function calls
* `n` execute current line and treats function as single execution step
* `c` continue execution until next breakpoint
* `p variable` print value of variable
* `h` list of commands
    * `h c` help on `c` command
* `q` quit the debugger

**Further Reading**

* [Python docs - pdb](https://docs.python.org/3/library/pdb.html)
* [pdb tutorial](https://github.com/spiside/pdb-tutorial)
* [common runtime errors](http://inventwithpython.com/blog/2012/07/09/16-common-python-runtime-errors/)
* [common beginner errors as a flowchart](http://pythonforbiologists.com/index.php/29-common-beginner-python-errors-on-one-page/)
* [Common pitfalls](https://stackoverflow.com/questions/1011431/common-pitfalls-in-python)
* [Python docs - Basic Logging Tutorial](https://docs.python.org/3/howto/logging.html)

<br>

### <a name="importing-program"></a>Importing program

* One can also `import` a program directly in Interpreter to test functions
* `if __name__ == "__main__":` construct
    * code inside that construct will be executed when program is intended to be run - ex: executing the program from command line
    * code inside that construct will NOT be executed when program is intended to be imported as module - ex: to use programs's functions
* A good practice is to put all code outside of functions inside a `main` function and call `main()` inside the `if __name__ == "__main__":` construct
* Note that `__name__` and `__main__` have two underscore characters as prefix and suffix

```python
#!/usr/bin/python3

# ----- function without arguments -----
def greeting():
    print("-----------------------------")
    print("         Hello World         ")
    print("-----------------------------")

# ----- function with arguments -----
def sum_two_numbers(num1, num2):
    sum = num1 + num2
    print("{} + {} = {}".format(num1, num2, sum))

# ----- function with return value -----
def num_square(num):
    return num * num

# ----- main -----
def main():
    greeting()
    sum_two_numbers(3, 4)

    my_num = 3
    print(num_square(2))
    print(num_square(my_num))

if __name__ == "__main__":
    main()
```

* When run as a program

```
$ ./functions_main.py
-----------------------------
         Hello World         
-----------------------------
3 + 4 = 7
4
9
```

* When importing

```python
>>> import functions_main

>>> functions_main.greeting()
-----------------------------
         Hello World         
-----------------------------

>>> functions_main.num_square()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: num_square() missing 1 required positional argument: 'num'

>>> functions_main.num_square(5)
25

>>> functions_main.main()
-----------------------------
         Hello World         
-----------------------------
3 + 4 = 7
4
9
```

**Further Reading**

* [Python docs - \_\_main\_\_](https://docs.python.org/3/library/__main__.html)
* [What does if \_\_name\_\_ == "\_\_main\_\_" do?](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)
* [Python packaging guide](https://packaging.python.org/en/latest/distributing/)
* [diveintopython3 - packaging](http://www.diveintopython3.net/packaging.html)
