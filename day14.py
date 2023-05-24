#Day 14 coding Statement : Write a program to reverse a given number
n=int(input("enter the number "))
l=len(str(n))-1
rev=0
while(n>0):
    a=n%10
    rev=rev+(a*(10**(l)))
    l=l-1
    n=n//10
print(f"required reversed number is {rev}")


'''
output:
enter the number 1234
required reversed number is 4321
'''
