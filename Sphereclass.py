# Program to calculate diameter, circumference, and volume of a sphere using class
class sphere():
    def diameter():
        print('Enter Redius of sphere ')
        r = float(input("Redius : "))
        d = 2*r
        print("Diameter os sphere is : ",d)

    def circum():
        print("Enter Redius of sphere ")
        r = float(input("Redius : "))
        cir = 2*3.14*r
        print("circumference :",cir)

    def volume():
        print("Enter Redius of sphere ")
        r = float(input("Redius : "))
        vol = (4*(3.14*r**3))/3
        print('Volume of sphere is : ',vol)
     


print("Program To calculate diameter, circumference, and volume of a sphere")
print('1.diameter\n2.circumference\n3.volume')
ch = int(input("Enter Your choice : "))
if ch == 1:
    sphere.diameter()
elif ch == 2:
    sphere.circum()
elif ch == 3:
    sphere.volume()
else:
    print("Wrong Input !!!!")
