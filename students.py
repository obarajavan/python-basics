
class Students:
    #constructor
    #runs automatically when an object is created
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def __str__(self):
        return f"The student name : {self.name} and age : {self.age} :course is {self.course}"
    def get_email(self):
        return f"{self.name}@emobilis.co.ke"
#create an object
#bject is an instant of a class
#ojectname=classname
student1=Students("James",17,"MIT")
student2=Students("Johm",18,"Cybersecurity")
print(student1)
print(student2)
#call our function
print(student1.get_email())
print(student2.get_email())