#dictionary-stores data in key:value pairs
student={
"name":"mary",
"age":17,
"course":"MIT"
}
print(student)
print(type[student])
#accessing the values
print(student["name"])
print(student["course"])
#adding key:value
student["city"]="nairobi"
print(student)
#updating a value
student["course"]="cyber security"
print(student)
#accessing all keys.keys()
print(student.keys())
#values()
print(student.values())
#items()
print(student.items())
#loop through all the keys
for x in student.keys():
    print(x)
#loop through all the values
for y in student.values():
    print(y)
#loop through all items
for x,y in student.items():
    print(x,":", y)