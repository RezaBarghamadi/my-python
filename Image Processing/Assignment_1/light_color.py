import cv2
image=cv2.imread("mo.jpg")
co=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
for i in range(co.shape[0]):
    for j in range(co.shape[1]):
        co[i, j] = 255 - co[i, j]
print(co.shape)
cv2.imshow("image",co)
cv2.waitKey()   
cv2.imwrite("light.jpg",co)