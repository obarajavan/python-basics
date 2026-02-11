class car:
    def __init__(self,Company,Model,Speed):
        self.Company=Company
        self.Model=Model
        self.Speed=Speed
    def __str__(self):
        return f"The car is from {self.Company} It is {self.Model} Model and has a top speed of {self.Speed} K/hr"
car1=car("Toyota","Supra",300)
car2=car("Dodge","Hellcat",270)
car3=car("Nissan","GT-R",290)
car4=car("BMW","M3",320)

print(car1)
print(car2)
print(car3)
print(car4)