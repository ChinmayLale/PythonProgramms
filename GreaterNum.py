# Program to calculate grater number out of 3 number
print('Enter 3 Numbers ')
n1 = int(input('1. '))
n2 = int(input('2. '))
n3 = int(input('3. '))
if n1 > n2 and n2 > n3:
    print('Gretest Number is : ',n1)
elif n2 > n1 and n2 > n3:
    print('Gretest Number is : ',n2)
elif n1==n2 and n2==n3:
    print('You Enterd Same Numbers')
else:
    print('Gretest Number is : ',n3)