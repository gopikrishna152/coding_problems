# Day 61 coding Statement: Chess Format
# Given the time control of a chess match as a+b, determine which format of chess out of the given 4 it belongs to.
# 1) Bullet if a+b < 3
#     2) Blitz if 3≤a+b≤10
#     3) Rapid if 11≤a+b≤60
#     4) Classical if 60 < a+b
#     Input Format
#     First line will contain T, number of testcases. Then the testcases follow.
#     Each testcase contains a single line of input, two integers a, b
#     Output Format
#     For each testcase, output in a single line, answer 1 for bullet, 2 for blitz, 3 for rapid, and 4 for classical format.
#     Sample Input 1
#     4
#     1 0
#     4 1
#     100 0
#     20 5
#     Sample Output 1
#     1
#     2
#     4
#     3
t=int(input("enter the test cases ")) 
while t>0:
    a,b=input("enter: ").split() 
    sum=int(a)+int(b) 
    if(sum<3):
        print("1") 
    elif(3<=sum<=10):
        print("2") 
    elif(11<=sum<=60): 
        print("3") 
    else:
        print("4") 
    t-=1 
    