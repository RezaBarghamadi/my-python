import qrcode

name=input("Enter Your Namme :")
phone=input("Enter Your Phone Number :")
finnal=[name,phone]
qr=qrcode.make(finnal)
qr.save("Your_qrcode.jpg")