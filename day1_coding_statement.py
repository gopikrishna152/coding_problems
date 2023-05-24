#Day 1 coding Statement: Write a program to identify if the character is a vowel or consonant.
vowels=['A','E','I','O','U','a','e','i','o','u']
a=input("enter")
if a.isalpha():
    if a in vowels:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid Input")


