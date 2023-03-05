print("Hi ")

name=input("Hi please Enter your Name")
lname=input("and please Enter your last name")
number=input("and please Enter your student number")
print ("your name is ",name )
print ("your lname is ",lname )
print ("your student number is ",number )

a=float(input("please Enter Math grade"))
b=float(input("please Enter chemistry grade"))
c=float(input("please Enter English  grade"))

print ("Youre Math grade ",a )
print ("Youre chemistry grade ",b )
print ("Youre English  grade ",c )
avg=(a+b+c)/3
print("your avg",avg)

if avg>=17:
    print("Grate")
elif 17>avg>12 :
    print("normal")
elif avg>12:
    print("failed")
