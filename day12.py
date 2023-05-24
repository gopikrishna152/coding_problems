#Day 12 coding Statement:  Write a program to find Sum of digits of a number
num=int(input("enter the number: "))
sum=0
while(num>0):
    a=num%10
    sum=sum+a
    num=num//10
print("the sum of digits is:",sum)