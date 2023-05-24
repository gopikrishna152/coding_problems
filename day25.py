# Day 25 coding Statement : Write a program to find Area of a circle
radius = float(input("enter the number"))


def area_of_circle(r):
    return 3.14*(r**2)


print(f"the area of the circle of radius {radius} is", area_of_circle(radius))
