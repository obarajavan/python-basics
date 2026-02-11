class employee:
    def __init__(self,Firstname,lastname,department,salary):
        self.Firstname=Firstname
        self.lastname=lastname
        self.salary=salary
        self.department=department
    def __str__(self):
        return f"The employee name is {self.Firstname} {self.lastname} and their salary is {self.salary}"
    def annual_salary(self):
        return f'{self.salary *12}'
    def fullname(self):
        return f'{self.Firstname} {self.lastname}'
employee1=(employee("Oscar","Daniel","ICT",20000))
employee2=employee("Jesse","Luvutse","Web developer", 50000)
employee3=employee("Noel","Sadiki","Cyber security",90000)
#access the attribute value
print(employee1)
print(employee1.department)
print(employee1.Firstname)
print(f' {employee1.Firstname} salary is {employee1.annual_salary()}')
print(employee2)
print(f' {employee2.Firstname} salary is {employee2.annual_salary()}')
print(employee1.fullname())