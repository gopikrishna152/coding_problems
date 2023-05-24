#Day 15 coding Statement : Write a program to identify if the number is Strong number or not
'''Description:Get a number as input from user and then check whether that number is a strong number or not. A number is said to be strong number if the sum of the factorial of each digit in the number is same as that of the number.'''
a=int(input("enter the number to check strong or not"))
N=a
rev=0
def factorial(x):
    if(x==1):
        return 1
    elif(x==0):
        return 1
    else:
        return x * factorial(x-1)

while(a>0):
    num=a%10
    req=factorial(num)
    rev=rev+req
    a=a//10
if N==rev:
    print("strong number")
else:
    print("not a strong number")