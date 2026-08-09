list=[1,5,3,2,4,"dibya"]

print(list)
#list1=list.sort()  if diffarent type are presnt in a type sort will not work

list1=[1,6,3,2,4,5]
list1.sort()
print(list1)
list1.reverse()
print(list1)
list1.append(7)
print(list1)
list1.insert(0,9)
print(list1)

poped=list1.pop()
print(poped)
print(list1)

removed=list1.remove(9)

print(removed)  #returns nothing
print(list1)




