import addition
import subtraction
import multiplication
import division

print("Welcome to the simple calculator in python")

a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
op=input("Enter the operator: ")    

if op=="+":
    addition.add(a,b)
elif op=="-":
    subtraction.sub(a,b)
elif op=="*":
    multiplication.mul(a,b)
elif op=="/":
    division.div(a,b)
else:
    print("Invalid operator ")                