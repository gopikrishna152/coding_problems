# Day 32 coding Statement : Write a Program to Remove vowels from a string
# Description
# Get a string as the input from the user and then remove all the vowel letters from the string and give the output.
# Input
# remove
# Output
# rmv
a = input("enter the string")
list1 = []
list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in a:
    if i in list:
        continue
    list1.append(i)
print("".join(list1))
 




# import java.util.Scanner;

# public class Main {

# 	public static void main(String[] args) {
		
#         String s = "prepinsta";
#         String s1 = "";
#         s1 = s.replaceAll("[aeiou]", ""); 
#         System.out.println("String after removing vowel : "+s1); 
# 	}

# }S













