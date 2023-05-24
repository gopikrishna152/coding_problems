#Day 21 coding Statement : Write a program to identify if the number is Palindrome or not 
n=int(input("enter the number"))
l=len(str(n))-1
rev,b=0,n
while(n>0):
    a=n%10
    rev=rev+(a*(10**l))
    l=l-1
    n=n//10
if(rev==b):
    print("palindrome")
else:
    print("not a palindrome")