# <a name="introduction"></a>Introduction

* [Installation](#installation)
* [Hello World example](#hello-world-example)
* [Python Interpreter](#python-interpreter)
* [Python Standard Library](#python-standard-library)


From [wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language))
>Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable clear programs on both a small and large scale

[Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum) is the author of Python programming language, and continues to oversee the Python development process

<br>

### <a name="installation"></a>Installation

* Get Python for your OS from official website - https://www.python.org/ 
    * Most Linux distributions come with Python by default
* See also [this guide](https://itsfoss.com/python-setup-linux/) for more detail as well as how to set up virtual environment, how to use **pip** (NEVER use **sudo pip** unless you know what you are doing)

<br>

* Examples presented here is for **Unix-like systems**, Python version 3 and uses **bash** shell
* You can also run Python code online
    * [pythontutor](http://www.pythontutor.com/visualize.html#mode=edit) - code execution in Python 2 and 3 versions, visualizing code flow and sample programs are among its features
    * [jupyter](https://try.jupyter.org/) - web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text
    * [ideone](https://ideone.com/) - online compiler and debugging tool which allows you to compile source code and execute it online in more than 60 programming languages
    * [Python Interpreter shell](https://www.python.org/shell/)
* It is assumed that you are familiar with command line. If not, check out [this basic tutorial on ryanstutorials](http://ryanstutorials.net/linuxtutorial/) and [this list of curated resources for Linux](https://github.com/learnbyexample/scripting_course/blob/master/Linux_curated_resources.md)

<br>

### <a name="hello-world-example"></a>Hello World example

Let's start with simple a Python program and how to run it

```python
#!/usr/bin/python3

print("Hello World")
```

The first line has two parts

* `/usr/bin/python3` is the path of Python interpreter
* `#!` called as **[shebang](https://en.wikipedia.org/wiki/Shebang_(Unix))**, directs the program loader to use the interpreter path provided

The third line prints the message `Hello World` with a newline character added by default by the `print` function

**Running Python program**

You can write the program using text editor like **gedit**, **[vim](http://yannesposito.com/Scratch/en/blog/Learn-Vim-Progressively/)** or [other editors](https://github.com/learnbyexample/Linux_command_line/blob/master/Working_with_Files_and_Directories.md#text-editors)  
After saving the file, give execute permission and run the program from a terminal

```
$ chmod +x hello_world.py

$ ./hello_world.py
Hello World
```

To find out path and version of Python in your system

```
$ type python3
python3 is /usr/bin/python3

$ python3 --version
Python 3.4.3
```

If you happen to follow a book/tutorial on Python version 2 or coming with Perl experience, it is a common mistake to forget () with `print` function

```python
#!/usr/bin/python3

print "Have a nice day"
```

* Depending on type of error, it may be easy to spot the mistake based on error messages printed on executing the program
* In this example, we get the appropriate `Missing parentheses` message

```
$ ./syntax_error.py 
  File "./syntax_error.py", line 3
    print "Have a nice day"
                          ^
SyntaxError: Missing parentheses in call to 'print'
```

* single line comments start with `#`
   * `#!` has special meaning only on first line of program
* we will see multiline comments in later chapters

```python
#!/usr/bin/python3

# Greeting message
print("Hello World")
```

**Further Reading**

* [Python docs - version 3](https://docs.python.org/3/index.html)
* [Different ways of executing Python programs](https://docs.python.org/3/using/windows.html#executing-scripts)
* [Where is Python used?](https://www.python.org/about/apps/)
* [Python docs - Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
* [Common syntax errors](https://opencs.uwaterloo.ca/python-from-scratch/7/7/transcript)

<br>

### <a name="python-interpreter"></a>Python Interpreter

* It is generally used to execute snippets of Python language as a means to learning Python or for debugging purposes
* The prompt is usually `>>>`
* Some of the topics in coming chapters will be complemented with examples using the Python Interpreter
* A special variable `_` holds the result of last printed expression
* One can type part of command and repeatedly press Up arrow key to match commands from history
* Press `Ctrl+l` to clear the screen, keeping any typed command intact
* `exit()` to exit

```python
$ python3
Python 3.4.3 (default, Oct 14 2015, 20:28:29) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("hi")
hi
>>> abc
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'abc' is not defined
>>> num = 5
>>> num
5
>>> 3 + 4
7
>>> 12 + _
19
>>> exit()
```

**Further Reading**

* [Python docs - Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
* [Python docs - Interpreter example](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)

<br>

### <a name="python-standard-library"></a>Python Standard Library

* [Python docs - library](https://docs.python.org/3/library/index.html)
* [pypi - repository of software for the Python programming language](https://pypi.python.org/pypi)

>The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming.

>Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs
