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
