# Smallest window that contains all characters of string itself
# Given a string, find the smallest window length with all distinct characters of the given string. For eg. str = “aabcbcdbca”, then the result would be 4 as of the smallest window will be “dbca” .
# Examples:

# Input: aabcbcdbca
# Output: dbca
# Explanation:
# Possible substrings = {aabcbcd, abcbcd,
#                        bcdbca, dbca....}
# Of the set of possible substrings 'dbca'
# is the shortest substring having all the
# distinct characters of given string.

# Input: aaab
# Output: ab
# Explanation:
# Possible substrings = {aaab, aab, ab}
# Of the set of possible substrings 'ab'
# is the shortest substring having all
# the distinct characters of given string.

def findsubstring(str):
    list, list1 = [], []
    count = 0
    for i in str:
        if i not in list:
            list.append(i)
            count += 1
    for j in range(1, len(str)-1):
        list1.append(str[j::])
    list = "".join(list)
    for i in list1:
        if len(i) == count:
            print(i)


str = input("enter the string ")
findsubstring(str.strip())
