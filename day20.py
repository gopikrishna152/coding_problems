#Day 20 coding Statement : Write a program to identify if the number is Prime number or not
n=int(input("enter the number")) 
count=2
for i in range(2,(n//2)+1):
    if(n%i==0):
        count=count+1
if(count==2):
    print("prime number")
else:
    print("not a prime number")