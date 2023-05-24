#Day 19 coding Statement : Write a program to identify if the number is Armstrong number or not
n=int(input("enter the number"))
l=len(str(n))
req=n
su=0
while(n>0):
    a=n%10
    su=su+(a**l) 
    n=n//10
if(su==req):
    print("armstrong")
else:
    print("not an armstrong ") 
'''
output:
        enter the number153
armstrong
'''