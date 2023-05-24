#Day 13 coding Statement:  Write a program to find Sum of N natural numbers
n=int(input("enter the number  "))
a=n
sum=0
while(n>0):
    sum+=n
    n=n-1
print(f"the sum of first {a} natural numbers is:",sum)


##output:enter the number5
#the sum of first 5 natural numbers is: 15