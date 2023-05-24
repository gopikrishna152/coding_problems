# Day 35 coding Statement: Write a Program to Count the sum of numbers in a string
# Description
# Get a string from the user and find the sum of numbers in the string.
# Input
# Hello56
# Output
# 11
a = input("enter the input ")
sum = 0
for i in a:
    if i.isnumeric():
        sum += int(i)
print("required sum of number is: ", sum)
