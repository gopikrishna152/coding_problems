#Day 9 coding Statement : Write a program to find Number of digits in an integer
a=int(input("enter the number"))
count=0
while(a>1):
    
    count=count+1
    a=a/10
print(count)