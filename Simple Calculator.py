def addition(num1, num2):
    return num1 + num2

def subtraction (num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

print ("Welcome to my python calculator, I hope you enjoy your experience!!! ")

username = input ("Please Enter your name...")

print ("Alright " + username + " Lets begin some arithmetic magic")

num1 =  float(input("Input the first number "))
num2 =  float(input("Input the second number "))
operation = input ("Enter the operation you want to carry out from +, -, *, / ")

if operation == "+":
    added = addition(num1, num2)
    print (added)
elif operation == "-":
    subtracted = subtraction(num1, num2)
    print (subtracted)
elif operation == "*":
    multiplied = multiplication(num1, num2)
    print (multiplied)
elif operation == "/":
    divided = division(num1, num2)
    print (divided)
else: 
    print ("Operation not available")