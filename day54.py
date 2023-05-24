# Day 54 coding Statement : Given an integer array of size N. Write Program to find whether Arrays are disjoint or not. Two arrays are said to be disjoint if they have no elements in common.
# Sample input 1:
# 4
# 2 -4 -1 -3
# 3
# 1 3 5
# Sample output 1:
# Disjoint
# Sample input 2:
# 5
# 1 5 -7 6 3
# 4
# 2 4 6 8
# Sample output 2:
# Not disjoint. ( 6 is common)
n1 = int(input("enter the size of the 1st array "))
arr1 = []
arr2 = []
for i in range(n1):
    a = int(input("enter the number"))
    arr1.append(a)
n2 = int(input("enter the size of the 2nd array "))
for i in range(n2):
    a = int(input("enter the number"))
    arr2.append(a)
if n2 > n1:
    for i in arr2:
        if i in arr1:
            print("not disjoint")
            break
    # print("disjoint ")
elif n1 > n2:
    for i in arr1:
        if i in arr2:
            print("not disjoint")
            break
else:
    print("disjoint ")
