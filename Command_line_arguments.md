# <a name="command-line-arguments"></a>Command line arguments

* [Known number of arguments](#known-number-of-arguments)
* [Varying number of arguments](#varying-number-of-arguments)
* [Using program name in code](#using-program-name-in-code)
* [Command line switches](#command-line-switches)

<br>

### <a name="known-number-of-arguments"></a>Known number of arguments

```python
#!/usr/bin/python3

import sys

if len(sys.argv) != 3:
    sys.exit("Error: Please provide exactly two numbers as arguments")
else:
    (num1, num2) = sys.argv[1:]
    total = int(num1) + int(num2)
    print("{} + {} = {}".format(num1, num2, total))
```

* Command line arguments given to Python program are automatically saved in `sys.argv` list
* It is a good idea to let the user know something went wrong
* As the program terminates with error message for wrong usage, use `sys.exit()` for error message (exit status 1) or a custom exit status number
* [Python docs - sys module](https://docs.python.org/3/library/sys.html#module-sys)

```
$ ./sum_of_two_numbers.py 2 3
2 + 3 = 5
$ echo $?
0

$ ./sum_of_two_numbers.py 2 3 7
Error: Please provide exactly two numbers as arguments
$ echo $?
1

$ ./sum_of_two_numbers.py 2 'x'
Traceback (most recent call last):
  File "./sum_of_two_numbers.py", line 9, in <module>
    total = int(num1) + int(num2)
ValueError: invalid literal for int() with base 10: 'x'
$ echo $?
1
```

<br>

### <a name="varying-number-of-arguments"></a>Varying number of arguments

```python
#!/usr/bin/python3

import sys, pathlib, subprocess

if len(sys.argv) < 2:
    sys.exit("Error: Please provide atleast one filename as argument")

input_files = sys.argv[1:]
files_not_found = []

for filename in input_files:
    if not pathlib.Path(filename).is_file():
        files_not_found.append("File '{}' not found".format(filename))
        continue

    line_count = subprocess.getoutput('wc -l < ' + filename)
    print("{0:40}: {1:4} lines".format(filename, line_count))

print("\n".join(files_not_found))
```

* When dealing with filenames obtained as user input, it is good to do a sanity check before processing
* [Python docs - pathlib](https://docs.python.org/3/library/pathlib.html)

```
$ ./varying_command_line_args.py
Error: Please provide atleast one filename as argument
$ echo $?
1

$ #selective output presented
$ ./varying_command_line_args.py *.py
calling_shell_commands.py               : 14   lines
for_loop.py                             : 6    lines
functions_default_arg_value.py          : 16   lines
functions.py                            : 24   lines
hello_world.py                          : 3    lines
if_elif_else.py                         : 22   lines
if_else_oneliner.py                     : 6    lines
shell_command_output_redirections.py    : 21   lines
...

$ ./varying_command_line_args.py hello_world.py xyz.py for_loop.py abc.py
hello_world.py                          : 3    lines
for_loop.py                             : 6    lines
File 'xyz.py' not found
File 'abc.py' not found
```

* use `os` module instead of `pathlib` for file checking if your Python version is not 3.4 and higher

```python
import os

if not os.path.isfile(filename):
    sys.exit("File '{}' not found".format(filename))
```

<br>

### <a name="using-program-name-in-code"></a>Using program name in code

```python
#!/usr/bin/python3

import sys, pathlib, subprocess, re

if len(sys.argv) != 2:
    sys.exit("Error: Please provide exactly one filename as argument")

program_name = sys.argv[0]
filename = sys.argv[1]

if not pathlib.Path(filename).is_file():
    sys.exit("File '{}' not found".format(filename))

if re.search(r'line_count.py', program_name):
    lc = subprocess.getoutput('wc -l < ' + filename)
    print("No. of lines in '{}' is: {}".format(filename, lc))
elif re.search(r'word_count.py', program_name):
    wc = subprocess.getoutput('wc -w < ' + filename)
    print("No. of words in '{}' is: {}".format(filename, wc))
else:
    sys.exit("Program name '{}' not recognized".format(program_name))
```

* Same program can be repurposed for different functionalities based on its name

```
$ ./line_count.py if_elif_else.py
No. of lines in 'if_elif_else.py' is: 22

$ ln -s line_count.py word_count.py
$ ./word_count.py if_elif_else.py 
No. of words in 'if_elif_else.py' is: 73

$ ln -s line_count.py abc.py
$ ./abc.py if_elif_else.py 
Program name './abc.py' not recognized

$ wc -lw if_elif_else.py
 22  73 if_elif_else.py
```

<br>

### <a name="command-line-switches"></a>Command line switches

```python
#!/usr/bin/python3

import argparse, subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help="file to be sorted", required=True)
parser.add_argument('-u', help="sort uniquely", action="store_true")
args = parser.parse_args()

if args.u:
    subprocess.call(['sort', '-u', args.file, '-o', args.file])
else:
    subprocess.call(['sort', args.file, '-o', args.file])
```

* using `argparse` module is a simpler way to build programs that behave like shell commands
* By default it adds a help option `-h` (short form) and `--help` (long form) as well as handles wrong usage

In this example:

* `-f` or `--file` option is declared as required option, it accepts an argument (which we treat as input file name in code)
* `-u` is an optional flag
* the `help` argument is used to specify text to be displayed for those options in help message

```
$ ./sort_file.py 
usage: sort_file.py [-h] -f FILE [-u]
sort_file.py: error: the following arguments are required: -f/--file

$ ./sort_file.py -h
usage: sort_file.py [-h] -f FILE [-u]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  file to be sorted
  -u                    sort uniquely

$ ./sort_file.py -f test_list.txt
$ cat test_list.txt
async_test
basic_test
input_test
input_test
output_test
sync_test

$ ./sort_file.py -f test_list.txt -u
$ cat test_list.txt
async_test
basic_test
input_test
output_test
sync_test

$ ./sort_file.py -f xyz.txt
sort: cannot read: xyz.txt: No such file or directory
```

* specifying positional arguments

```python
#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('num1', type=int, help="first number")
parser.add_argument('num2', type=int, help="second number")
args = parser.parse_args()

total = args.num1 + args.num2
print("{} + {} = {}".format(args.num1, args.num2, total))
```

* more readable approach than manually parsing `sys.argv` as well as default help and error handling
* type conversions required can be specified while building parser itself

```
$ ./sum2nums_argparse.py 
usage: sum2nums_argparse.py [-h] num1 num2
sum2nums_argparse.py: error: the following arguments are required: num1, num2

$ ./sum2nums_argparse.py -h
usage: sum2nums_argparse.py [-h] num1 num2

positional arguments:
  num1        first number
  num2        second number

optional arguments:
  -h, --help  show this help message and exit

$ ./sum2nums_argparse.py 3 4
3 + 4 = 7

$ ./sum2nums_argparse.py 3 4 7
usage: sum2nums_argparse.py [-h] num1 num2
sum2nums_argparse.py: error: unrecognized arguments: 7
```


**Further Reading**

* [Python docs - argparse tutorial](https://docs.python.org/3/howto/argparse.html#id1)
* [Python docs - argparse module](https://docs.python.org/3/library/argparse.html#module-argparse)
* [argparse examples with explanation](https://stackoverflow.com/questions/7427101/dead-simple-argparse-example-wanted-1-argument-3-results)
* [Python docs - getopt module](https://docs.python.org/3/library/getopt.html#module-getopt)
