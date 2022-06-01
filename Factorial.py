# Factorial Program 
num = int(input('Enter A Number which factorial you want'))
fact = 1
for i in range (1,num+1):
    fact = fact * i
print('The Factorial of '+str(num)+' is : ',fact)