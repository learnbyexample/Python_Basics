# <a name="executing-external-commands"></a>Executing external commands

* [Calling Shell commands](#calling-shell-commands)
* [Calling Shell commands with expansion](#calling-shell-commands-with-expansion)
* [Getting command output and redirections](#getting-command-output-and-redirections)

The sample output shown in this chapter may be different based on your username, working directories, etc

<br>

### <a name="calling-shell-commands"></a>Calling Shell commands

```python
#!/usr/bin/python3

import subprocess

# Executing external command 'date'
subprocess.call('date')

# Passing options and arguments to command
print("\nToday is ", end="", flush=True)
subprocess.call(['date', '-u', '+%A'])

# another example
print("\nSearching for 'hello world'", flush=True)
subprocess.call(['grep', '-i', 'hello world', 'hello_world.py'])
```

* `import` statement here is used to load the `subprocess` module, which is part of the [Python standard library](https://docs.python.org/3/library/index.html)
* the `call` function from `subprocess` module is one of the ways to execute external commands
* By passing `True` to `flush` argument (default is `False`) we ensure that our message is printed before `subprocess.call`
* For passing arguments, list of strings is passed instead of single string

```
$ ./calling_shell_commands.py 
Tue Jun 21 18:35:33 IST 2016

Today is Tuesday

Searching for 'hello world'
print("Hello World")
```

**Further Reading**

* [Python docs - subprocess](https://docs.python.org/3/library/subprocess.html)
* [Python docs - os.system](https://docs.python.org/3/library/os.html#os.system)
    * [difference between os.system and subprocess.call](https://www.quora.com/Whats-the-difference-between-os-system-and-subprocess-call-in-Python)
* [Python docs - import statement](https://docs.python.org/3/reference/simple_stmts.html#import)

<br>

### <a name="calling-shell-commands-with-expansion"></a>Calling Shell commands with expansion

```python
#!/usr/bin/python3

import subprocess

# Executing command without shell expansion
print("No shell expansion when shell=False", flush=True)
subprocess.call(['echo', 'Hello $USER'])

# Executing command with shell expansion
print("\nshell expansion when shell=True", flush=True)
subprocess.call('echo Hello $USER', shell=True)

# escape quotes if it is part of command
print("\nSearching for 'hello world'", flush=True)
subprocess.call('grep -i \'hello world\' hello_world.py', shell=True)
```

* By default, `subprocess.call` will not expand [shell wildcards](https://github.com/learnbyexample/Linux_command_line/blob/master/Shell.md#wildcards), perform [command substitution](http://mywiki.wooledge.org/CommandSubstitution), etc
* This can be overridden by passing `True` value for `shell` argument
* Note that the entire command is now passed as string and not as a list of strings
* Quotes need to be escaped if they clash between command string and quotes within the command itself
* Use `shell=True` only if you are sure of the command being executed, else it could be a [security issue](https://stackoverflow.com/questions/3172470/actual-meaning-of-shell-true-in-subprocess)
    * [Python docs - subprocess.Popen](https://docs.python.org/3/library/subprocess.html#popen-constructor)

```
$ ./shell_expansion.py 
No shell expansion when shell=False
Hello $USER

shell expansion when shell=True
Hello learnbyexample

Searching for 'hello world'
print("Hello World")
```

* In certain cases, escaping quotes can be avoided by using combination of single/double quotes as shown below

```python
# use alternate quotes, like this
subprocess.call('grep -i "hello world" hello_world.py', shell=True)

# or this
subprocess.call("grep -i 'hello world' hello_world.py", shell=True)
```

* [Shell command redirections](https://github.com/learnbyexample/Linux_command_line/blob/master/Shell.md#redirection) can be used as usual

```python
# use variables for clarity and to avoid long strings within call function
cmd = "grep -h 'test' report.log test_list.txt > grep_test.txt"
subprocess.call(cmd, shell=True)
```

**Workaround to avoid using shell=True**

```python
>>> import subprocess, os
>>> subprocess.call(['echo', 'Hello', os.environ.get("USER")])
Hello learnbyexample
0
```

* `os.environ.get("USER")` gives back the value of environment variable `USER`
* `0` is the exit status, meaning success. It is a caveat of python interpreter which displays return value too

<br>

### <a name="getting-command-output-and-redirections"></a>Getting command output and redirections

```python
#!/usr/bin/python3

import subprocess

# Output includes any error messages also
print("Getting output of 'pwd' command", flush=True)
curr_working_dir = subprocess.getoutput('pwd')
print(curr_working_dir)

# Get status and output of command executed
# Exit status other than '0' is considered as something gone wrong
ls_command = 'ls hello_world.py xyz.py'
print("\nCalling command '{}'".format(ls_command), flush=True)
(ls_status, ls_output) = subprocess.getstatusoutput(ls_command)
print("status: {}\noutput: '{}'".format(ls_status, ls_output))

# Suppress error messages if preferred
# subprocess.call() returns status of command which can be used instead
print("\nCalling command with error msg suppressed", flush=True)
ls_status = subprocess.call(ls_command, shell=True, stderr=subprocess.DEVNULL)
print("status: {}".format(ls_status))
```

* Output of `getstatusoutput()` is of `tuple` data type, more info and examples in later chapters
* `getstatusoutput()` and `getoutput()` are legacy functions
* Use newer functions for more features and secure options
    * [Python docs - subprocess.check_output](https://docs.python.org/3/library/subprocess.html#subprocess.check_output)
    * [Python docs - subprocess.run](https://docs.python.org/3/library/subprocess.html#subprocess.run)

```
$ ./shell_command_output_redirections.py 
Getting output of 'pwd' command
/home/learnbyexample/Python/python_programs

Calling command 'ls hello_world.py xyz.py'
status: 2
output: 'ls: cannot access xyz.py: No such file or directory
hello_world.py'

Calling command with error msg suppressed
hello_world.py
status: 2
```
