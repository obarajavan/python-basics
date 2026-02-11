class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        return f'hello'
    def supermethod(self):
        return f'hello form a method in super class'

class Dog(Animal):
    def speak(self):
        return ('bark bark')
    def chrome(self):
        return f'hello form a method in dog class'

mydog=Dog("bob",9)
print(mydog.name)
print(mydog.supermethod())
print(mydog.speak())
print(mydog.chrome())
#create a cat object
class Cat(Animal):
    def speak(self):
        return ('meow meow')
    def silver(self):
        return f'hello form a method in cat class'
mycat=Cat("Oscar",1)
#call the speak method
print(mycat.speak())
#call me th supermethod
print(mycat.silver())