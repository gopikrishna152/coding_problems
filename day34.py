# Day 34 coding Statement: Write a Program to Remove brackets from an algebraic expression
# Description
# Get an algebraic expression as input from the user and then remove all the brackets in that.
# Input
# 7x+(2*y)
# Output
# 7x+2*y
a = input("enter the equation")
list = []
for i in a:
    if (i == '(') or (i == ')'):
        continue
    else:
        list.append(i)
print("output", "".join(list))
