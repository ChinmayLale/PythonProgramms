# Program to check the addition of entered numbers is even or odd
n1 = int(input('Enter 1st Number : '))
n2 = int(input('Enter 2nd Number : ')) 
s = n1 + n2
if s % 2 == 0:
    print("Sum is Even")
else:
    print('Sum is odd')

    