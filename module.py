#module-python file that contains python code, it can have functions,variables
#etc that you want to include in your file
#import the module
import math as fm
print(fm.sqrt(25))
print(fm.pi)
print(fm.floor(3.46))
print(fm.ceil(3.46))
import random
#generate in btwn 5-14
print(random.randint(5,14))
#generate random num btwn 0-1
print(random.random())
import datetime
#generate current date and time
print(datetime.datetime.now())
print(datetime.datetime.now().year)

x=datetime.datetime.now()
print(x.year)
print(x.month)
print(x.hour)

