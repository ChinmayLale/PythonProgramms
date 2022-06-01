# Union of lists
def union(list1,list2):
   result = list(set(list1 + list2))
   return result

l1 = [1,2,3,4,5]
l2 = [2,4,6,8,10]
l3= union(l1,l2)

print("l1: ",l1)
print("l2: ",l2)
print("Union of two l1 and l2 without repetition : ",l3)