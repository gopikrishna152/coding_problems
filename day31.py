# Day 31 coding Statement : Write a Program to Toggle each character in a string
# Description
# Get an input string from user and then convert the lower case of alphabets to upper case and all upper-case alphabets into lower case.
# Input
# Hello
# Output
# hELLO
n = input("enter the string ")
for i in range(len(n)):
    if (n[i] >= 'A' and n[i] <= 'Z'):
        n = n[:i] + chr(ord(str[i]) + ord('a') - ord('A')) + n[i + 1:]
    elif (n[i] >= 'a' and n[i] <= 'z'):

        n = n[:i] + chr(ord(str[i]) + ord('A') - ord('a')) + n[i + 1:]
print(n)
