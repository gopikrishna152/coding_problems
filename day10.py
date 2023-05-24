







#Day 10 coding Statement:  Write a program to find Factorial of a number
a=int(input("enter the number "))
def factorial(x):
    if(x==1):
        return 1
    elif(x==0):
        return 1
    else:
        return x*factorial(x-1)
print("the value of factorial is ",factorial(a))