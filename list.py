#list=used to show multiple elements in a single variable
#list is ordered,changeable and allows duplicates
students=["johari","mary","keter","jane","allison"]
mynums=[78,67,90,45,90]
print(students)
print(mynums)
print(type(students))
print(type(mynums))
#len()-number of list items
print(len(students))
print(len(mynums))
#accessing list item
print(students[0])
print(students[4])
#modifying list item
print(students)
students[1]="Angela"
print(students)
#list methods,append(),remove(),pop()
#append
students.append("john")
print(students)
#remove-removes a specific item
students.remove("jane")
print(students)
#insert()-adds an element at specific index
students.insert(1,"lewis")
print(students)
#looping through a list
for x in students:
    print(x)
#
courses=["MIT","PYTHON","HTML","JAVASCRIPT","PYCHARM","VSCODE"]
print(courses)
for y in courses:
    print(y)