a=float(input("Please enter your weight in kilograms :"))
b=float(input("and enter your height in meters : "))

# print("Your weight is  :",a)

# print("Your height is   :",b)

bmi=a/(b*b)

if bmi<18.6:
    print("undeweight")
elif 18.5<bmi<24.9:
    print("Normal")
elif 25<bmi<29.9:
    print("overweight")
elif 30<bmi<34.9:
    print ("obestity")
elif 35<bmi<39:
    print (" Extreme obestity")