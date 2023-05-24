# Day 52 coding Statement: Given an integer array of size N, write a program to reverse the array
# Sample input 1:
# 4
# 2 4 1 3
# Sample output 1:
# 3 1 4 2
# Sample input
# 5
# 1 5 7 5 3
# Sample output 2
# 3 5 7 5 1
a = int(input("enter the size"))
list = []
for i in range(a):
    list.append(int(input("enter the element: ")))
print(list)
print(list[::-1])
