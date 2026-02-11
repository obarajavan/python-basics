#function with return keyword return a value

#function that adds two numbers
def addTwoNumbers(a,b):
    sum=a+b
    return sum
#calling the function amd storing the returned value in a variable
result=addTwoNumbers(30,50)
print("the sum is",result)
#way wo
print(addTwoNumbers(20,79))
#function that multiplies 3 numbers
def multithreenum(x,y,z):
    multiple=x*y*z
    return multiple
product=multithreenum(20,30,40)
print("The multiple is",product)
#function that checks if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} The number is even.")
else:
    print(f"{num} The number is odd.")
#function that finds maximuml
def maximum(j,k):
    return max(j,k)
print(maximum(45,67))