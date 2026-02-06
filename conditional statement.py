#if statement
"""
if statement specifies a block of code to be executed if the condition  is true
if condition:
            block of code to be executed if condition is true
"""
x=5
if x<10:
  print(f"{x}  is less than 10")
  """ if...else
  is condition:
             block of code to be executed if the condition is true
else:
    block of code to be executed if the condition is false
  """
  #a program that checks if a user is eligible to vote
  age=12
if age>=18:
   print("you are eligible to vote")
else:
    print("you are not eligible to vote")
#a  program that asks user for age and checks if they can drive
user_age=int(input("enter your age"))
if user_age>=18:
    print("you can drive")
else:
    print("you cannot drive")
 #a  program that asks user for a number and check if
#the number is even or odd .hintevennumber%2==0
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} The number is even.")
else:
    print(f"{num} The number is odd.")
    # a program that asks the user for two number and prints the greater number

    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    if num1> num2:
        print("The greater number is:" ,num1)
    else:
        print("The greater number is:", num2)



