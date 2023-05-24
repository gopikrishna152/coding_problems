#Day 16 coding Statement : Write a program to identify if the number is Perfect number or not 
n=int(input("enter the numebr :"))  
sum=0
for i in range(1,(n//2)+1):
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print("perfect number")
else:
    print("not a perfect number")