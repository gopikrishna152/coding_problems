# Day 27 coding Statement : Write a program to find the double of the given number without using arithmetic operator
n = int(input("enter the number "))


def double(n):
    for i in range(n, 2*n):
        n = n+1
    return n


print(double(n))
