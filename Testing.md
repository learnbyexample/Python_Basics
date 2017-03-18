# <a name="testing"></a>Testing

* [assert statement](#assert-statement)
* [Using assert to test a program](#using-assert-to-test-a-program)
* [Using unittest framework](#using-unittest-framework)
* [Using unittest.mock to test user input and program output](#using-unittest.mock-to-test-user-input-and-program-output)
* [Other testing frameworks](#other-testing-frameworks)


<br>

### <a name="assert-statement"></a>assert statement

* `assert` is primarily used for debugging purposes like catching invalid input or a condition that shouldn't occur
* An optional message can be passed for descriptive error message than a plain **AssertionError**
* It uses [raise statement](https://docs.python.org/3/tutorial/errors.html#raising-exceptions) for implementation
* `assert` statements can be skipped by passing the `-O` [command line option](https://docs.python.org/3/using/cmdline.html)
* **Note** that `assert` is a statement and not a function

```python
>>> assert 2 ** 3 == 8
>>> assert 3 > 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError

>>> assert 3 > 4, "3 is not greater than 4"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: 3 is not greater than 4
```

Let's take a factorial function as an example:

```python
>>> def fact(n):
        total = 1
        for num in range(1, n+1):
            total *= num
        return total

>>> assert fact(4) == 24
>>> assert fact(0) == 1
>>> fact(5)
120

>>> fact(-3)
1
>>> fact(2.3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in fact
TypeError: 'float' object cannot be interpreted as an integer
```

* `assert fact(4) == 24` and `assert fact(0) == 1` can be considered as sample tests to check the function

Let's see how `assert` can be used to validate arguments passed to the function:

```python
>>> def fact(n):
        assert type(n) == int and n >= 0, "Number should be zero or positive integer"
        total = 1
        for num in range(1, n+1):
            total *= num
        return total
    
>>> fact(5)
120
>>> fact(-3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in fact
AssertionError: Number should be zero or positive integer
>>> fact(2.3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in fact
AssertionError: Number should be zero or positive integer
```

<br>

The above factorial function can also be written using [reduce](https://docs.python.org/3/library/functools.html#functools.reduce)

```python
>>> def fact(n):
        assert type(n) == int and n >= 0, "Number should be zero or positive integer"
        from functools import reduce
        from operator import mul
        return reduce(mul, range(1, n+1), 1)
    

>>> fact(23)
25852016738884976640000
```

Above examples for demonstration only, for practical purposes use `math.factorial` which also gives appropriate exceptions

```python
>>> from math import factorial
>>> factorial(10)
3628800

>>> factorial(-5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: factorial() not defined for negative values
>>> factorial(3.14)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: factorial() only accepts integral values
```

**Further Reading**

* [Python docs - assert](https://docs.python.org/3/reference/simple_stmts.html#assert)
* [What is the use of assert in Python?](https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python)
* [Is Unit Testing worth the effort?](https://stackoverflow.com/questions/67299/is-unit-testing-worth-the-effort)

<br>

### <a name="using-assert-to-test-a-program"></a>Using assert to test a program

In a limited fashion, one can use `assert` to test a program - either within the program (and later skipped using the `-O` option) or as separate test program(s)

Let's try testing the **palindrome** program we saw in [Docstrings](./Docstrings.md#palindrome-example) chapter

```python
#!/usr/bin/python3

import palindrome

assert palindrome.is_palindrome('Madam')
assert palindrome.is_palindrome("Dammit, I'm mad!")
assert not palindrome.is_palindrome('aaa')
assert palindrome.is_palindrome('Malayalam')

try:
    assert palindrome.is_palindrome('as2')
except ValueError as e:
    assert str(e) == 'Characters other than alphabets and punctuations'

try:
    assert palindrome.is_palindrome("a'a")
except ValueError as e:
    assert str(e) == 'Less than 3 alphabets'

print('All tests passed')
```

* There are four different cases tested for **is_palindrome** function 
    * Valid palindrome string
    * Invalid palindrome string
    * Invalid characters in string
    * Insufficient characters in string
* Both the program being tested and program to test are in same directory
* To test the **main** function, we need to simulate user input. For this and other useful features, test frameworks come in handy

```
$ ./test_palindrome.py 
All tests passed
```

<br>

### <a name="using-unittest-framework"></a>Using unittest framework

This section requires understanding of [classes](https://docs.python.org/3/tutorial/classes.html)

<br>

```python
#!/usr/bin/python3

import palindrome
import unittest

class TestPalindrome(unittest.TestCase):

    def test_valid(self):
        # check valid input strings
        self.assertTrue(palindrome.is_palindrome('kek'))
        self.assertTrue(palindrome.is_palindrome("Dammit, I'm mad!"))
        self.assertFalse(palindrome.is_palindrome('zzz'))
        self.assertFalse(palindrome.is_palindrome('cool'))

    def test_error(self):
        # check only the exception raised
        with self.assertRaises(ValueError):
            palindrome.is_palindrome('abc123')

        with self.assertRaises(TypeError):
            palindrome.is_palindrome(7)

        # check error message as well
        with self.assertRaises(ValueError) as cm:
            palindrome.is_palindrome('on 2 no')
        em = str(cm.exception)
        self.assertEqual(em, 'Characters other than alphabets and punctuations')

        with self.assertRaises(ValueError) as cm:
            palindrome.is_palindrome('to')
        em = str(cm.exception)
        self.assertEqual(em, 'Less than 3 alphabets')

if __name__ == '__main__':
    unittest.main()
```

* First we create a subclass of **unittest.TestCase** (inheritance)
* Then, different type of checks can be grouped in separate functions - function names starting with **test** are automatically called by **unittest.main()**
* Depending upon type of test performed, **assertTrue, assertFalse, assertRaises, assertEqual, etc** can be used
* [An Introduction to Classes and Inheritance](http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/)
* [Python docs - unittest](https://docs.python.org/3/library/unittest.html)
    * [Command-Line Interface](https://docs.python.org/3/library/unittest.html#command-line-interface)
    * [Test Discovery](https://docs.python.org/3/library/unittest.html#test-discovery)
    * [Organizing test code, setUp and tearDown](https://docs.python.org/3/library/unittest.html#organizing-test-code)

```
$ ./unittest_palindrome.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK

$ ./unittest_palindrome.py -v
test_error (__main__.TestPalindrome) ... ok
test_valid (__main__.TestPalindrome) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

<br>

### <a name="using-unittest.mock-to-test-user-input-and-program-output"></a>Using unittest.mock to test user input and program output

This section requires understanding of decorators, [do check out this wonderful intro](https://stackoverflow.com/questions/739654/how-to-make-a-chain-of-function-decorators-in-python/1594484#1594484)

<br>

A simple example to see how to capture `print` output for testing

```python
>>> from unittest import mock
>>> from io import StringIO

>>> def greeting():
        print('Hi there!')

>>> def test():
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            greeting()
            assert mock_stdout.getvalue() == 'Hi there!\n'
    
>>> test()
```

One can also use `decorators`

```python
>>> @mock.patch('sys.stdout', new_callable=StringIO)
    def test(mock_stdout):
        greeting()
        assert mock_stdout.getvalue() == 'Hi there!\n'
```

<br>

Now let's see how to emulate `input`

```python
>>> def greeting():
        name = input('Enter your name: ')
        print('Hello', name)
    
>>> greeting()
Enter your name: learnbyexample
Hello learnbyexample

>>> with mock.patch('builtins.input', return_value='Tom'):
        greeting()
    
Hello Tom
```

<br>

Combining both

```python
>>> @mock.patch('sys.stdout', new_callable=StringIO)
    def test_greeting(name, mock_stdout):
        with mock.patch('builtins.input', return_value=name):
            greeting()
            assert mock_stdout.getvalue() == 'Hello ' + name + '\n'
    
>>> test_greeting('Jo')
```

<br>

Having seen basic input/output testing, let's apply it to main function of **palindrome**

```python
#!/usr/bin/python3

import palindrome
import unittest
from unittest import mock
from io import StringIO

class TestPalindrome(unittest.TestCase):

    @mock.patch('sys.stdout', new_callable=StringIO)
    def main_op(self, tst_str, mock_stdout):
        with mock.patch('builtins.input', side_effect=tst_str):
            palindrome.main()
        return mock_stdout.getvalue()

    def test_valid(self):
        for s in ('Malayalam', 'kek'):
            self.assertEqual(self.main_op([s]), s + ' is a palindrome\n')

        for s in ('zzz', 'cool'):
            self.assertEqual(self.main_op([s]), s + ' is NOT a palindrome\n')

    def test_error(self):
        em1 = 'Error: Characters other than alphabets and punctuations\n'
        em2 = 'Error: Less than 3 alphabets\n'

        tst1 = em1 + 'Madam is a palindrome\n'
        self.assertEqual(self.main_op(['123', 'Madam']), tst1)

        tst2 = em2 + em1 + 'Jerry is NOT a palindrome\n'
        self.assertEqual(self.main_op(['to', 'a2a', 'Jerry']), tst2)

if __name__ == '__main__':
    unittest.main()
```

* Two test functions - one for testing valid input strings and another to check error messages
* Here, **side_effect** which accepts iterable like list, compared to **return_value** where only one input value can be mocked
* For valid input strings, the **palindrome** main function would need only one input value
* For error conditions, the iterable comes handy as the main function is programmed to run infinitely until valid input is given
* [Python docs - unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
    * [patchers](https://docs.python.org/3/library/unittest.mock.html#the-patchers)
* [An Introduction to Mocking in Python](https://www.toptal.com/python/an-introduction-to-mocking-in-python)
* [PEP 0318 - decorators](https://www.python.org/dev/peps/pep-0318/)
* [decorators](https://pythonconquerstheuniverse.wordpress.com/2012/04/29/python-decorators/)

```
$ ./unittest_palindrome_main.py 
..
----------------------------------------------------------------------
Ran 2 tests in 0.003s

OK
```

<br>

### <a name="other-testing-frameworks"></a>Other testing frameworks

* [pytest](http://doc.pytest.org/en/latest/getting-started.html)
* [Python docs - doctest](https://docs.python.org/3/library/doctest.html)
* [Python test automation](https://github.com/atinfo/awesome-test-automation/blob/master/python-test-automation.md)
* [Python Testing Tools Taxonomy](https://wiki.python.org/moin/PythonTestingToolsTaxonomy)
* [Python test frameworks](http://docs.python-guide.org/en/latest/writing/tests/)

Test driven development (TDD)

* [Test-Driven Development with Python](http://chimera.labs.oreilly.com/books/1234000000754/index.html)
* [learn Python via TDD](https://github.com/gregmalcolm/python_koans)
