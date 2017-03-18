# <a name="file-handling"></a>File handling

* [open function](#open-function)
* [Reading files](#reading-files)
* [Writing to files](#writing-to-files)
* [Inplace editing with fileinput](#inplace-editing-with-fileinput)

<br>

### <a name="open-function"></a>open function

* syntax: open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

```python
>>> import locale
>>> locale.getpreferredencoding()
'UTF-8'
```

* We'll be seeing these modes in this chapter
    * `r` open file for reading
    * `w` open file for writing
    * `a` open file for appending
* default is text mode, so passing 'r' and 'rt' are equivalent
    * for binary mode, it would be 'rb', 'wb' and so on
* `locale.getpreferredencoding()` gives default encoding being used
* [Python docs - open](https://docs.python.org/3/library/functions.html#open)
* [Python docs - standard encodings](https://docs.python.org/3/library/codecs.html#standard-encodings)

<br>

### <a name="reading-files"></a>Reading files

```python
#!/usr/bin/python3

# open file, read line by line and print it
filename = 'hello_world.py'
f = open(filename, 'r', encoding='ascii')

print("Contents of " + filename)
print('-' * 30)
for line in f:
    print(line, end='')

f.close()

# 'with' is a simpler alternative, automatically handles file closing
filename = 'while_loop.py'

print("\n\nContents of " + filename)
print('-' * 30)
with open(filename, 'r', encoding='ascii') as f:
    for line in f:
        print(line, end='')
```

* default encoding is usually 'UTF-8', use 'ascii' where applicable
* using `with` and file handle name as `f` is usual convention

```bash
$ ./file_reading.py
Contents of hello_world.py
------------------------------
#!/usr/bin/python3

print("Hello World")


Contents of while_loop.py
------------------------------
#!/usr/bin/python3

# continuously ask user input till it is a positive integer
usr_string = 'not a number'
while not usr_string.isnumeric():
    usr_string = input("Enter a positive integer: ")
```

**If file doesn't exist**

```python
#!/usr/bin/python3

with open('xyz.py', 'r', encoding='ascii') as f:
    for line in f:
        print(line, end='')
```

* Error if file is not found

```bash
$ ./file_reading_error.py 
Traceback (most recent call last):
  File "./file_reading_error.py", line 3, in <module>
    with open('xyz.py', 'r', encoding='ascii') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'xyz.py'
$ echo $?
1
```

* read entire file content as single string using `read()`

```python
>>> f = open('hello_world.py', 'r', encoding='ascii')
>>> f
<_io.TextIOWrapper name='hello_world.py' mode='r' encoding='ascii'>
>>> print(f.read())
#!/usr/bin/python3

print("Hello World")

```

* read line by line using `readline()`

```python
>>> f = open('hello_world.py', 'r', encoding='ascii')
>>> print(f.readline(), end='')
#!/usr/bin/python3
>>> print(f.readline(), end='')

>>> print(f.readline(), end='')
print("Hello World")

>>> f.close()
>>> print(f.readline(), end='')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

* read all lines of file as list using `readlines()`
    * note the plural form

```python
>>> f = open('hello_world.py', 'r', encoding='ascii')
>>> all_lines = f.readlines()
>>> all_lines
['#!/usr/bin/python3\n', '\n', 'print("Hello World")\n']
```

* check if file is closed or not

```python
>>> f = open('hello_world.py', 'r', encoding='ascii')

>>> f.closed
False

>>> f.close()
>>> f.closed
True
```

<br>

### <a name="writing-to-files"></a>Writing to files

```python
#!/usr/bin/python3

with open('new_file.txt', 'w', encoding='ascii') as f:
    f.write("This is a sample line of text\n")
    f.write("Yet another line\n")
```

* Use the `write()` method to print a string to files
* To add text to an existing file, use 'a' mode instead of 'w'

```bash
$ ./file_writing.py
$ cat new_file.txt 
This is a sample line of text
Yet another line
```

<br>

### <a name="inplace-editing-with-fileinput"></a>Inplace editing with fileinput

```python
#!/usr/bin/python3

import fileinput

with fileinput.input(inplace=True) as f:
    for line in f:
        line = line.replace('line of text', 'line')
        print(line, end='')
```

* The files to be modified are specified as [Command line arguments](./Command_line_arguments.md) when the program is run
* Note that `print` function has to be used instead of `f.write`
* Since the line read every iteration already has newline character, **end** is assigned empty string
* [Python docs - fileinput](https://docs.python.org/3/library/fileinput.html)

```bash
$ ./inplace_file_editing.py new_file.txt
$ cat new_file.txt 
This is a sample line
Yet another line

$ # to change all files in current directory ending with .txt, use
$ ./inplace_file_editing.py *.txt

$ # stdin can also be passed as input, inplace gets disabled
$ echo 'a line of text' | ./inplace_file_editing.py
a line
```

* specifying filenames and backup extensions

```python
# To specify filenames within the program itself
with fileinput.input(inplace=True, files=('file1.txt', 'file2.txt')) as f:

# To create backup of unmodified files, pass an extension to backup parameter
with fileinput.input(inplace=True, backup='.bkp') as f:
```
