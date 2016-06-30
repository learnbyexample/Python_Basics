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
