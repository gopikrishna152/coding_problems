#Day 17 coding Statement : Write a program to find the Factors of a number 
n=int(input("enter the number"))
for i in range(1,(n//2)+1):
    if(n%i==0):
        print(i,end=",")
print(f"{n}")