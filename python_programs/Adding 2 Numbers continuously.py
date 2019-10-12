while(1):
    # Store input numbers
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')
    # Add two numbers
    sum = float(num1) + float(num2)
    # Display the sum
    print('The sum of {0} and {1} is {2}\n'.format(num1, num2, sum))
    c=input("Do you want to continue :(y/n)")
    if(c=='y' or c=='Y'):
        continue
    else:
        break
