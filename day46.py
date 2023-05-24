# Day 46 coding Statement: Write Program to find sum of elements in an array
# Description
# Get an array as the input from the user and find the sum of the elements.
# Input
# Enter the size of array
# 3
# Enter the elements of array
# 5 10 15
# Output
# 30

n = int(input("enter the size of the array"))
list = []
sum = 0
for i in range(n):
    a = int(input("enter the numbers"))
    sum += a
    list.append(a)
print(f"the sum of the elements in an array {list} is {sum}")
