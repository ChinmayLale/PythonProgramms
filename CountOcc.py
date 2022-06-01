# Program to count occ of specific word in string
stri = input('Enter String')
w = input("enter word which you want find")
cou = 0
spli = stri.split(' ')
for i in range (0,len(spli)):
    if w == spli[i]:
        cou = cou+1 

print('The Occurunce os the word is : ',cou)
