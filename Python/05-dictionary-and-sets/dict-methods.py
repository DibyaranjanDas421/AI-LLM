student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}

#1 get
print(student["name"])
print(student.get("name"))

print(student.get("name")) # retunrs noone if not present
# print(student["name1"]) # retunr error
#2 keys
print(student.keys())
#3 values
print(student.values())
#4 items
print(student.items())
#5 update
student.update({"age":24})
print(student)

#6 pop()
student.pop("age")
print(student)
#7 popitem()
student.popitem()
print(student)

#9 setdefault()
student.setdefault("city","Mumbai")
print(student)

#10 copy()

new_student=student.copy()
print(new_student)

#11 clear

new_student.clear()
print(new_student)

#12

keys=["a","b","c",1]
print(type(keys))

d=dict.fromkeys(keys,0)
print(d)