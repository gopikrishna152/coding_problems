# Smallest window in a String containing all characters of other String
# Given two strings, string and pattern, the task is to find the smallest substring in string containing all characters of pattern.

# Examples:

# Input: string = “this is a test string”, pattern = “tist”
# Output: “t stri”
# Explanation: “t stri” contains all the characters of pattern.

# Input: string = “geeksforgeeks”, pattern = “ork”
# Output: “ksfor”


def findsubstring(str):
    list, list1 = [], []
    count = 0
    for i in str:
        if i not in list:
            list.append(i)
            count += 1
    for j in range(1, len(str)-1):
        list1.append(str[j::])
    print(list1)


str = input("enter the string ")
findsubstring(str.strip())
