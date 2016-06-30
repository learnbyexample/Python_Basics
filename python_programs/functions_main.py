#!/usr/bin/python3

# ----- function without arguments -----
def greeting():
    print("-----------------------------")
    print("         Hello World         ")
    print("-----------------------------")

# ----- function with arguments -----
def sum_two_numbers(num1, num2):
    sum = num1 + num2
    print("{} + {} = {}".format(num1, num2, sum))

# ----- function with return value -----
def num_square(num):
    return num * num

# ----- main -----
def main():
    greeting()
    sum_two_numbers(3, 4)

    my_num = 3
    print(num_square(2))
    print(num_square(my_num))

if __name__ == "__main__":
    main()
