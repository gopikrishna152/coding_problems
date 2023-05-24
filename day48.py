# Day 48 coding Statement: Write Program to remove duplicate elements in an array
# Description
# Get an array as input from the user and then remove all the duplicate elements in that array.
# Input
# Enter the size of array
# 5
# Enter the elements of array
# 35 35 45 60 60
# Output
# 35 45 60
n = int(input("enter the size of an array: "))
lis = []
for i in range(n):
    a = int(input(f"enter the {i+1} number"))
    lis.append(a)
print(list(set(lis)))
