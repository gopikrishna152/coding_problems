# Day 33 coding Statement: Write a Program to check if String is a palindrome or not
# Description*
# Get an input string from the user and then check whether it is a palindrome string or not
# Input
# noon
# Output
# Palindrome
# Input
# Talent
# Output
# Not a Palindrome
a = input("enter the string: ")
low = 0
high = len(a)-1
let = True
while high > low:
    if a[high] != a[low]:
        let = False
        break
    low += 1
    high -= 1
if (let == True):
    print("palindrome")
else:
    print("not a palindrome")
