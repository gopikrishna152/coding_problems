# Day 49 coding Statement : Given 2 integer arrays X and Y of same size. Consider both arrays as vectors and print the minimum scalar product (Dot product) of 2 vectors.
# Sample input 1 :
# 4
# 1 2 3 4
# 5 6 7 8
# Sample output 1 :
# 60
# Explanation :
# (4*5 + 3*6 + 2*7 + 1*8) = 60
# Sample input 2 :
# 4
# -1 -2 -3 -4
# 5 6 -7 -8
a = int(input("enter the size: "))
list1, list2 = [], []
ele1 = 0
for i in range(a):
    ele = int(input(f"enter the {i+1} numbers"))
    list1.append(ele)
for i in range(a):
    ele = int(input(f"enter the {i+1} numbers"))
    ele1 = ele1 + ele*list1[-i-1]
    list2.append(ele)
print(list2)
print(ele1)
