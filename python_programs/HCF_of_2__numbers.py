print "~~Program to find HCF of two numbers~~"
print ""
def hcf():
    
    x = int(raw_input("Enter first number: "))
    y = int(raw_input("Enter second number: "))
    a = max(x,y)
    b = min(x,y)
    while int(a) % int(b) != 0:
        c = a%b
        temp = b         #To rearrange  the values of a,b and c.
        b = c
        a = temp
    else:
        print " HCF of the given numbers is : %s " %(b)
    print ""
    z = raw_input("Enter Y to play again or any key to quit. ")
    if z.upper() == 'Y':
        hcf()
    else:
        pass
hcf()
