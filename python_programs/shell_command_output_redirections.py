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
