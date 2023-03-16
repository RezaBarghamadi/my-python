import math
import sys

print("Hi Welcome to My Calculator :)")
for i in range(100):
    print("Are you ready to run this program")
    print("yes Or no")
    comment=input()
    if comment=="yes":
        print("OK lets Go")
    else:
        print("The End please Close")
        sys.exit(0)

    print ("this List are: ")
    print("Computing ")
    print("+")
    print("-")
    print("/")
    print("*")
    print("^")
    print("sqr")
    print("sin")
    print("cos")
    print("tan")
    print("cot")
    print("fa")
    print("exit")
    print ("enter your oprator")
    op=input()
    if op=="exit":
        break  
    if op=="+" or op=="-" or op=="*" or op=="/":
        a=float(input("Enter  first number :"))
        b=float(input("Enter  second number :"))
    else:

        a=float(input("Enter Number :"))

    if op=="+":
        res=a+b
 
    elif op=="-":
        res=a-b
    elif op=="*":
        res=a*b
    elif op=="^":
        res=a*a
    elif op=="sin":
        res=math.sin(math.radians(a))
    elif op=="cos":
        res=math.cos(math.radians(a))
    elif op=="tan":
        res=math.tan(math.radians(a))
    elif op=="cot":
     res=math.cot(math.radians(a))         
    elif op=="sqr":
        res=math.sqrt(a)
    elif op=="fa":
        res=math.factorial(a)
    elif op=="-":
        res=a-b
 
    elif op=="/":
        if b==0:
            res="Your denominator is zero"
    else:
        res=a/b

    
    print("Your action ",res)