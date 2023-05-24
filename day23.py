# Day 23 coding Statement : Write a program to Replace all 0’s with 1 in a given integer
# Input

# 310020

# Output

# 311121

a = int(input('enter the number'))
list = []
for i in str(a):
    if (i == '0'):
        list.append('1')
    else:
        list.append(i)
print(int("".join(list)))
