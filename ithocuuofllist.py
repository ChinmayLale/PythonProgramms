# Program to find ith occ in list
test_str = "Hello world this is python "

count = 0

for i in test_str:
	if i == 'o':
		count = count + 1

print ("Count of o in string is : "+ str(count))
