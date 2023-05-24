# Day 36 coding Statement: Write a Program to Capitalize the first and last letter of each word of a string
# Description
# Get a string from the user and then change the first and last letter to uppercase.
# Input
# programming
# Output
# ProgramminG
a = input("enter the string ")
l = len(a)
list = []
result = ""
for i in range(l):
    if (i == 0):
        result += a[0].upper()
    elif (i == l-1):
        result += a[-1].upper()
    else:
        result += a[i]
print(result)
