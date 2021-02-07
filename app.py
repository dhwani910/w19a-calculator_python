import addition
import subtraction
import multiplication
import division


def method():
    while True:
        print("Welcome to the simple calculator in python")
        op=input("Enter the operator: ")  
        thislist = []
        a = True

        while a == True:
            n1 = input("enter the number: ")
            print("To calculate type '=': ")
            if n1 == "=":
                a = False
            else:
                n1 = float(n1)
                thislist.append(n1)  

        if op=="+":
            answer = addition.add(thislist)
            print("result: " + str(answer))
            print(thislist)
        elif op=="-":
            answer = subtraction.sub(thislist)
            print("result: " + str(answer))
        elif op=="*":
            answer = multiplication.mul(thislist)
            print("result: " + str(answer))
        elif op=="/":
            answer = division.div(thislist)
            print("result: " + str(answer))
        else:
            print("Invalid operator")  

        print(" ")  

method()                       
                      
            




  

               