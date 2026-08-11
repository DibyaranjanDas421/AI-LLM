A = {1, 2, 3, 4}
B = {3, 4, 5, 6}


#1 union

print(A.union(B))

#2 intersection
print(A.intersection(B))

#3 diffarence

print(A.difference(B))

#4 symmetric diffarence

print(A.symmetric_difference(B))


C={1,2}
D={1,2,3,4}


#5 subset
print(C.issubset(D))

#6 superset
print(D.issuperset(C))

E={1,2,3}
F={4,5,6}

#7 disjoint

print(E.isdisjoint(F))
