import cv2



image=cv2.imread("images.jpg")
image_2=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for i in range(101):
    image_2[i, 80-i:100-i] = 0

for i in range(80,100 ):
  image_2[i, 0:100-i]=0

print(image_2.shape)
cv2.imshow("image",image_2)
cv2.imwrite("ded.jpg",image_2)