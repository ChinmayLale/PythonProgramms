# Program to find length of list using reccursion
def lenoflist(a):
    if not a:
        return 0
    return 1 + lenoflist(a[1::1])

a = []
i = 0
c = None
print ("enter elements in list and enter 'exit' after all elements are entered")
while c != 'exit':
    i = i+1
    c = input(str(i)+". ")
    a.append(c)

print(a)
len=lenoflist(a)
print('Length of list is : '+str(len))
