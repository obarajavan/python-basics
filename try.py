"""
try:
   block of code that can cause error
except:
   #code that runs if error happens
"""
try:
    num=int(input("enter a number"))
    print(10/num)
except:
    print("you cannot divide a number a zero")
#another example
try:
    print(x)
except NameError:
    print("the variable is not defined")
try:
  with open('abcd.txt','r') as y:
    print(y.read())
except FileNotFoundError:
      print('File not found')
