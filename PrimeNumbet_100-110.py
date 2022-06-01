# Program to check prime numbers between 100-110
check = False
for i in range(100,111):
    for j in range(2,i):
        if i%j == 0:
            break
        else:
            print(i)

