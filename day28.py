# Day 28 coding Statement : Write a Program to reverse a string.
a = input("enter the string")
list = []
for i in a:
    list.append(i)
list = list[::-1]
print(f"the reverse of {a} is ", ('').join(list))
