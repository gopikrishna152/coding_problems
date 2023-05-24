# Day 45 coding Statement: Write Program to find smallest and largest element in an array
# Description
# Get an array as input from the user and then find the smallest and largest element in the array.
# Input
# Enter the size of array:
# 5
# Enter the elements:
# 10 20 5 40 30
# Output
# Smallest Number:
# 5
# Largest Number:
# 40 
a=int(input("enter the no of elements")) 
list=[] 
for i in range(a):
    ele=int(input("enter the element"))  
    list.append(ele) 
print(f"the list is {list}")
max=list[0]
min=list[0] 
for ele in list:
    if(ele>max):
        max=ele
    if(ele<min):
        min=ele
print(f"the max ele is {max}\nthe min ele is {min}")