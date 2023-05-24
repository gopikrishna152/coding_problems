# Day 43 coding Statement: Write Program to find the array type
# Description
# Get an array as input from the user and check the type of the array, whether it is odd, even or mixed type.
# Input
# Enter size of array:
# 3
# Enter elements
# 1 3 5
# Output
# Odd

list = []
a = int(input("enter the size of an array: "))
for i in range(a):
    b = int(input("enter the elements "))
    list.append(b)
if (len(list) % 2 == 0):
    print("even")
else:
    print("odd")
