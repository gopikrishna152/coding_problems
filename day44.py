# Day 44 coding Statement: Write Program to find number of even and odd elements in an array
# Description
# Get an array as input from the user and then count the number of even and odd elements present in the array.
# Input
# Enter size of array
# 4
# Enter the elements:
# 1 3 4 5
# Output
# Number of even elements:
# 1
# Number of odd elements:
# 3
a = int(input("enter the size"))
list = []
even = 0
for i in range(a):
    b = int(input("enter the element to insert "))
    list.append(b)
    if (b % 2 == 0):
        even += 1
print(f"no of even elements are: {even}")
print(f"no of odd elements are {len(list)-even}")
