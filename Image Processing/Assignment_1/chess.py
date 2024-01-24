import cv2

my_image=cv2.imread("ches.jpg")
print(my_image.shape)

for i in range(50,100):
    for j in range(0,50):
            my_image[i,j]=0

for i in range(150,200):
    for j in range(0,50):
            my_image[i,j]=0

for i in range(250,300):
    for j in range(0,50):
            my_image[i,j]=0

for i in range(350,400):
    for j in range(0,50):
            my_image[i,j]=0   
for i in range(450,500):
    for j in range(0,50):
            my_image[i,j]=0  
for i in range(550,600):
    for j in range(0,50):
            my_image[i,j]=0   


for i in range(150,200):
    for j in range(100,150):
            my_image[i,j]=0    

for i in range(0,50):
    for j in range(50,100):
            my_image[i,j]=0

 #my_image[0:50,0:50]=0
cv2.imshow("chess",my_image)
cv2.waitKey()