# Program to store keys and values of string in dict
w = []
s = input('Enter a string')
d = {}
w = s.split()
for s in w:
    chr = s[0]
    if chr not in d:
        d[chr] = []
    d[chr].append(s)
print(d)
for k,v in d.items():
    print(k," : ",v)
    