#Day 6 coding Statement:  Write a program to find the Quadrants in which coordinates lie
x=int(input("enter the value of x"))
y=int(input("enter the value of x"))
if(x>0 and y>0):
    print("the point lies in first quadrant")
elif(x>0 and y<0):
    print("the point lies in fourth quadrant")
elif(x<0 and y>0):
    print("the point lies in second quadrant")
else:
    print("the point lies in third quadrant")