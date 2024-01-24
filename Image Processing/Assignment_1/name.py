import cv2



name=cv2.imread("name.jpg")

print(name.shape)
name[100:500,180:210]=0
name[100:140,218:400]=0
name[140:200,370:400]=0
name[200:240,218:400]=0

name[243:295,213:250]=0

name[300:350,250:290]=0
name[350:400,290:320]=0
name[400:450,320:360]=0
name[450:500,360:400]=0
cv2.imshow("reza",name)
cv2.waitKey()
cv2.imwrite("res_name.jpg",name)