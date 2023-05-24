# Day 50 coding Statement: Given an integer array of size N. Write Program to find sum of positive square elements in the array.
# Sample input 1:
# 4 1 2 3 4
# Sample output 1:
# 30
# Explanation:
# (1 + 4 + 9 + 16) = 30
n = int(input("enter the number :"))
sum = 0
list1 = []
for i in range(n):
    a = int(input("enter the elements: "))
    sum = sum+a**2
    list1.append(a)
print(sum)
