# Day 42 coding Statement: Write Program to check if two arrays are the same or not
# Description
# Get two arrays as the input from the user and check whether it is the same or not .
# Input
# Enter the size of first array:
# 3
# Enter the size of second array:
# 3
# Enter elements of first array:
# 1 2 3
# Enter elements of second array:
# 1 2 3
# Output
# Same

list1, list2 = [], []
a = int(input("enter the size of array: "))
b = int(input("enter the size of second array: "))
if a != b:
    print("not same")
else:
    for i in range(a):
        c = input("enter the elements to insert into array ")
        list1.append(c)
    for i in range(b):
        c = input("enter the elements to insert into array ")
        list2.append(c)
    if list1 == list2:
        print("same")
    else:
        print("not same")
