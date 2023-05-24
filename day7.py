#Day 7 coding Statement:  Write a program to find Number of days in a given month of a given year
#Input
#Enter month : 2
#Enter year : 2000
#Output
#29
month=int(input("enter the month"))
year=int(input("enter the year"))
if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    print("31 days")
elif(month==4 or month==6 or month==9 or month==11 ):
    print("30 days")
else:
    if (year%4==0 or year%100==0):
        print("29 days")
    else:
        print("28 days")
