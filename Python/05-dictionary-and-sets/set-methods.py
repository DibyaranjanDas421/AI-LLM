s={1,2,3}

#1 add()
s.add(4)

print(s)

#2 upadte()
s.update([4,5,6])
print(s)

#3 remove()
s.remove(1)
print(s)
# s.remove(9) # gives error if no key

#4 discard()
s.discard(9) # dose not return error

#5 pop() removes arbitary elemnts
s.pop()
print(s)

#6 clear()
s.clear()
print(s)