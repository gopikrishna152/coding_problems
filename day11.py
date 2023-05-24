#Day 11 coding Statement:  Write a program to find Fibonacci series up to n
n=int(input("enter the series"))
a,b=0,1
print("fibonacci :",a,b,end=" ")
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
#output:
  
#enter the series6
#fibonacci : 0 1 1 2 3 5