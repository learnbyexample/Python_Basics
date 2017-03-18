# <a name="docstrings"></a>Docstrings

* [Style guide](#style-guide)
* [Palindrome example](#palindrome-example)

<br>

### <a name="style-guide"></a>Style guide

Paraphrased from [Python docs - coding style](https://docs.python.org/3/tutorial/controlflow.html#intermezzo-coding-style)

* Use 4-space indentation, and no tabs.
    * 4 spaces are a good compromise between small indentation (allows greater nesting depth) and large indentation (easier to read). Tabs introduce confusion, and are best left out.
* Wrap lines so that they don’t exceed 79 characters.
    * This helps users with small displays and makes it possible to have several code files side-by-side on larger displays.
* Use blank lines to separate functions and classes, and larger blocks of code inside functions.
* When possible, put comments on a line of their own.
* Use docstrings.
* Use spaces around operators and after commas
* Name your classes and functions consistently;
    * the convention is to use CamelCase for classes and lower_case_with_underscores for functions and methods

**Style guides**

* [PEP 0008](https://www.python.org/dev/peps/pep-0008/)
* [Google - pyguide](https://google.github.io/styleguide/pyguide.html)
* [elements of python style](https://github.com/amontalenti/elements-of-python-style)
* [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/) - handbook of best practices

<br>

### <a name="palindrome-example"></a>Palindrome example

```python
#!/usr/bin/python3

"""
Asks for user input and tells if string is palindrome or not

Allowed characters: alphabets and punctuations .,;:'"-!?
Minimum alphabets: 3 and cannot be all same

Informs if input is invalid and asks user for input again
"""

import re

def is_palindrome(usr_ip):
    """
    Checks if string is a palindrome

    ValueError: if string is invalid

    Returns True if palindrome, False otherwise
    """

    # remove punctuations & whitespace and change to all lowercase
    ip_str = re.sub(r'[\s.;:,\'"!?-]', r'', usr_ip).lower()

    if re.search(r'[^a-zA-Z]', ip_str):
        raise ValueError("Characters other than alphabets and punctuations")
    elif len(ip_str) < 3:
        raise ValueError("Less than 3 alphabets")
    else:
        return ip_str == ip_str[::-1] and not re.search(r'^(.)\1+$', ip_str)

def main():
    while True:
        try:
            usr_ip = input("Enter a palindrome: ")
            if is_palindrome(usr_ip):
                print("{} is a palindrome".format(usr_ip))
            else:
                print("{} is NOT a palindrome".format(usr_ip))
            break
        except ValueError as e:
            print('Error: ' + str(e))

if __name__ == "__main__":
    main()
```

* The first triple quoted strings marks the docstring for entire program
* The second one inside `is_palindrome()` is specific for that function

```
$ ./palindrome.py 
Enter a palindrome: as2
Error: Characters other than alphabets and punctuations
Enter a palindrome: "Dammit, I'm mad!"
"Dammit, I'm mad!" is a palindrome

$ ./palindrome.py 
Enter a palindrome: a'a
Error: Less than 3 alphabets
Enter a palindrome: aaa
aaa is NOT a palindrome
```

* Let's see how docstrings can be used as help
* Notice how docstring gets automatically formatted

```python
>>> import palindrome
>>> help(palindrome)

Help on module palindrome:

NAME
    palindrome - Asks for user input and tells if string is palindrome or not

DESCRIPTION
    Allowed characters: alphabets and punctuations .,;:'"-!?
    Minimum alphabets: 3 and cannot be all same
    
    Informs if input is invalid and asks user for input again

FUNCTIONS
    is_palindrome(usr_ip)
        Checks if string is a palindrome
        
        ValueError: if string is invalid
        
        Returns True if palindrome, False otherwise
    
    main()

FILE
    /home/learnbyexample/python_programs/palindrome.py
```

* One can get help on functions directly too

```python
>>> help(palindrome.is_palindrome)

Help on function is_palindrome in module palindrome:

is_palindrome(usr_ip)
    Checks if string is a palindrome
    
    ValueError: if string is invalid
    
    Returns True if palindrome, False otherwise
```

* and of course test the functions

```python
>>> palindrome.is_palindrome('aaa')
False
>>> palindrome.is_palindrome('Madam')
True

>>> palindrome.main()
Enter a palindrome: 3452
Error: Characters other than alphabets and punctuations
Enter a palindrome: Malayalam
Malayalam is a palindrome
```

**Further Reading**

* [docstring formats](http://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format)
* [exception message capturing](http://stackoverflow.com/questions/4690600/python-exception-message-capturing)
