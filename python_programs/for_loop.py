number=int(input("which number's multiplication table do you want"))
for i in range(1, 11):
    mul_table = number * i
    print("{} * {} = {}".format(number, i, mul_table))
