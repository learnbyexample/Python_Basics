# <a name="getting-user-input"></a>Getting User input

* [Integer input](#integer-input)
* [Floating point input](#floating-point-input)
* [String input](#string-input)

<br>

### <a name="integer-input"></a>Integer input

```python
#!/usr/bin/python3

usr_ip = input("Enter an integer number: ")

# Need to explicitly convert input string to desired type
usr_num = int(usr_ip)
sqr_num = usr_num * usr_num

print("Square of entered number is: {}".format(sqr_num))
```

* Let us test the program by giving an integer number and a string
* [Python docs - integer-literals](https://docs.python.org/3/reference/lexical_analysis.html#integer-literals)

```
$ ./user_input_int.py 
Enter an integer number: 23
Square of entered number is: 529

$ ./user_input_int.py 
Enter an integer number: abc
Traceback (most recent call last):
  File "./user_input_int.py", line 6, in <module>
    usr_num = int(usr_ip)
ValueError: invalid literal for int() with base 10: 'abc'
```

<br>

### <a name="floating-point-input"></a>Floating point input

```python
#!/usr/bin/python3

usr_ip = input("Enter a floating point number: ")

# Need to explicitly convert input string to desired type
usr_num = float(usr_ip)
sqr_num = usr_num * usr_num

# Limit the number of digits after decimal points to 2
print("Square of entered number is: {0:.2f}".format(sqr_num))
```

* The [E scientific notation](https://en.wikipedia.org/wiki/Scientific_notation#E_notation) can also be used when required
* [Python docs - floating-point-literals](https://docs.python.org/3/reference/lexical_analysis.html#floating-point-literals)
* [Python docs - floatingpoint](https://docs.python.org/3/tutorial/floatingpoint.html)

```
$ ./user_input_float.py 
Enter a floating point number: 3.232
Square of entered number is: 10.45

$ ./user_input_float.py 
Enter a floating point number: 42.7e5
Square of entered number is: 18232900000000.00

$ ./user_input_float.py 
Enter a floating point number: abc
Traceback (most recent call last):
  File "./user_input_float.py", line 6, in <module>
    usr_num = float(usr_ip)
ValueError: could not convert string to float: 'abc'
```

<br>

### <a name="string-input"></a>String input

```python
#!/usr/bin/python3

usr_name  = input("Hi there! What's your name? ")
usr_color = input("And your favorite color is? ")

print("{}, I like the {} color too".format(usr_name, usr_color))
```

* No need any type conversion for string and no newline character to be taken care unlike Perl

```
$ ./user_input_str.py 
Hi there! What's your name? learnbyexample
And your favorite color is? blue
learnbyexample, I like the blue color too
```

