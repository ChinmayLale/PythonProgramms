# Program to find area of different shapes 
import math
def circle():
    r=int(input("Enter redius of circle"))
    area = math.pi*r*r
    print('Area of circle is : ',area)

def square():
    s = int(input('Enter lenght of Side of square'))
    a = s*s
    print('area of square is : ',a)

def rectangle():
    l = int(input('Enter length  of rectangle'))
    b = int(input('Enter breadth  of rectangle'))
    a = l*b
    print('area of rectangle is : ',a)

def parallelogram():
    l = int(input('Enter base  of parallelogram'))
    b = int(input('Enter height  of parallelogram'))
    a = l*b
    print('area of parallelogram is : ',a)

def triangle():
    h = int(input('Enter height  of triangle'))
    b = int(input('Enter base  of triangle'))
    area = (h*b)*0.5
    print('Area of triangle is : ',area);7


print("This is the program to calculate area of shspes\n")
print('1.Circle\n2.Square\n3.Rectangle\n4.Parallelogram\n5.Triangle')
ch = int(input('Enter Your Choice'))
if ch == 1:
    circle()
elif ch == 2:
    square()
elif ch == 3:
    rectangle()
elif ch == 4:
    parallelogram()
elif ch == 5:
    triangle()
else:
    print('Wrong choice')