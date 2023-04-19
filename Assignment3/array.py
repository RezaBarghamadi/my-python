my_array=[]

for i in range(1,100):
    x=int(input("Enter Your Number :"))
    if x in my_array:
        print("This number is repeated ")
    else:
        my_array.append(x)
        print(my_array)