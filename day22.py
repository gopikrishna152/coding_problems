# Day 22 coding Statement : Write a program to express a number as a sum of two prime numbers
n = int(input("enter the number"))
arr = []
result = 0


def isprime(n):
    count = 2
    for i in range(2, (n//2)+1):
        if (n % i == 0):
            count = count+1
    if (count == 2):
        return True
    else:
        return False


for i in range(2, (n)):
    if isprime(i) == 1:
        arr.append(i)
for i in range(0, len(arr)):
    for j in range((i+1), len(arr)):
        if (arr[i]+arr[i] == n):
            print(f"yes we can express {n} as {arr[i]}+{arr[i]}")
            result = result+1
        elif (arr[i] + arr[j] == n):
            print(f"yes we can express {n} as {arr[i]}+{arr[j]}")
            result = result+1
if (result == 0):
    print("cannot express as the sum of prime numbers")
