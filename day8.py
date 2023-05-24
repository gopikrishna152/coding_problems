#Day 8 coding Statement:  Write a program to find roots of a quadratic equation
import math
a=int(input("enter the coefficient of x^2"))
b=int(input("enter the coefficient of x"))
c=int(input("enter the coefficient of constant"))
if a==0:
    print("a cannot be zero")
    
descriminant=b*b-4*a*c
root1=(-b+math.sqrt(descriminant))/2*a
root2=(-b-math.sqrt(descriminant))/2*a
if(root1==root2):
    print("roots are equal")
    print("root1=root2=",root1)
else:
    print("roots are not equal") 
    print("root1 is",root1)
    print("root2 is ",root2)
