f = open('E:\SE_SEM-2\Python\hello.txt','+r')
data = f.read()
cap = data.upper()
print(cap)
f.write(cap)

f.close()