#tuples are ordered,unchangeable and allow duplicates
courses=("MIT","PYTHON","HTML","JAVASCRIPT","PYCHARM","VSCODE")
print(courses)
print(type(courses))
#accessimg the item
print(courses[1])
#len()
print(len(courses))
#loop
for course in courses:
    print(course)
#tuple()
digit=tuple((91,27,34.90,67,45))
print(digit)
print(type(digit))
#loop
for num in digit:
    print(num)