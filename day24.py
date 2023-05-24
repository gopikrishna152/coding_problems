# Day 24 coding Statement : Write a program to print Pyramid pattern using stars
# *
# ***
# *****
# *******
a = int(input("enter the no of rows"))
for i in range(0, a):
    for j in range(i, i+1):
        print(((2*i)+1) * "*")
    print("", end="")
