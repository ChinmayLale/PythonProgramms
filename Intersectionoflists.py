# program to find intersection of list

def intersection(lst1, lst2):
	lst3 = [value for value in lst1 if value in lst2]
	return lst3


list1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
list2 = [9, 9, 74, 21, 45, 11,]
print(intersection(list1, list2))
