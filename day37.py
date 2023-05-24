# Day 37 coding Statement: Write a Program to calculate the Frequency of characters in a string
# Description
# Get a string as the input from the user and find the frequency of characters in the string.
# Input
# program
# Output
# The frequency of a is 1
# The frequency of g is 1
# The frequency of m is 1
# The frequency of o is 1
# The frequency of p is 1
# The frequency of r is 2
a = input("enter the string: ")
for i in a:
    freq = a.count(i)

    print(f"the frequency of  {i} is {freq}")
