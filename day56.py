# Day 56 coding Statement: Write Program to find whether the numbers of an array be made equal
# Description
# Check whether the numbers of array be made equal or not
# For eg, for the following input it should print yes because
# 50*2*3, 75*2*2 and 150*2 are equal to 300 in all cases. So array numbers can be made equa
# Input
# 3
# 50 75 150
# Output
# Yes
n = int(input("enter the size of an array "))
list1 = []


def convert(a, n):
    for i in range(n):
        while (a[i] % 2 == 0):
            a[i] = a[i]/2
        while (a[i] % 3 == 0):
            a[i] = a[i]/3
    for i in range(n):
        if a[i] != a[0]:
            return False
    return True


for i in range(n):
    a = int(input("enter the number in array "))
    list1.append(a)
if convert(list1, n):
    print("yes")
else:
    print("no")
