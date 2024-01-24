import cv2

my_image=cv2.imread("1.jpg")
my_image_1=cv2.cvtColor(my_image,cv2.COLOR_BGR2GRAY)

print(my_image_1.shape)
print(my_image_1[50,200])
my_image_1[0:25,0: 368]=0
my_image_1[0:355,1: 20]=0
my_image_1[0:355,350: 368]=0
my_image_1[330:355,1: 368]=0
cv2.imshow("reza",my_image_1)
cv2.waitKey()
cv2.imwrite("res.jpg",m)