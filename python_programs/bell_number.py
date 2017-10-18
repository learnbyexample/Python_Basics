#program to print bell number

#Bell Number:-Let S(n, k) be total number of partitions of n elements into k sets. The value of n’th Bell Number is sum of S(n, k) for k = 1 to n. Value of S(n, k) can be defined recursively as, S(n+1, k) = k*S(n, k) + S(n, k-1)

#The code to print the bell triangle is as follows-

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

n=int(input("enter the number of bell"))     #taking value from the user

bell=0 #initialising bell to 'zero'

k=0    #initialising k to 'zero'

for i in range(0,n):

    for j in range(0,i+1):

        if j==0 and i>0:

            print(bell,'',end='')        #printing first number of each line

        else:

            k=(i**2)+1+bell              #to generate other numbers of line

            print(k,'',end='')           #printing other number in lines

            bell=k                       #updating value of bell 

    print('\n')                          #for moving into next lines           

print("last number of bell is",bell)    


