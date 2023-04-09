print(" Hi This app receives seconds and converts them to hours")
print("please Enter Your Seconds : ")
sec=int(input())

print("Your Seconds is : " ,sec)
hr=sec//3600
m=(sec%3600)//60
s=(sec%60)

print(sec, "seconds"," = ",hr,":",m,":",s)