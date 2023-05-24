#Day 18 coding Statement : Write a program to Add two fractions 
n1=int(input("enter the numerator of number1 ")) 
d1=int(input("enter the denominator of number1 "))
n2=int(input("enter the numerator of number2 "))
d2=int(input("enter the denominator of number2 ")) 
if(d1==d2):
    n3=n1+n2
    if(n3%d1==0):
        n3=n3//d1
        print(f"{n3}/{d1}")
    else:
        print(f"{n3}/{d1}")

else:
     n3 = (n1*d2) + (n2*d1) 
     d3 = (d1*d2)
     print(f"{n3}/{d3}")

'''
output:
enter the numerator of number1 4
enter the denominator of number1 5
enter the numerator of number2 6
enter the denominator of number2 4
46/20
'''