#functions-perform a specific task
"""
def fuctionname():
block of code
"""
def demo():
    print("hello goodafternoon")
#calling the function
demo()
demo()
#anothr function
def greeting(name):
    print("hello",name)
#calling the function
greeting("John")
greeting("Otieno")
#a function with multiple parameters
def StudentInfo(first_name,age=18):
    print(f"hello {first_name} you are {age} years old")
#calling the function
StudentInfo("David",17)
StudentInfo("Oscar",18)
StudentInfo("Allison",18)
StudentInfo("cate")
#function that calculates area of a rectangle
def areaofarectangle(l,w):
    area=l*w
    print(f"The area of rectangle with length{l} and width {w} is {area}")
#calling the function
areaofarectangle(70,56)
areaofarectangle(10,20)
#a function that calculates area of a circle  .a=3.14*r*r
def areaofacircle(r,a=3.14):
    area=a*r*r
    print(f"The Area of a Circle with pie {a} and radius {r} is {area}")
#calling the function
areaofacircle(20)
areaofacircle(30)
