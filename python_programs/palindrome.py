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
