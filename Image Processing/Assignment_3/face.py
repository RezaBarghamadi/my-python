import cv2

image=cv2.imread("reza.jpg")

my_stiker=cv2.imread("01.png")
image_g=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

face_detector=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
#location Facess

faces_location=face_detector.detectMultiScale(image_g)
for face in faces_location:
    x,y,w,h=face
    stiker=cv2.resize(my_stiker,[w,h])
    image[y:y+h ,x:x+w]=stiker


cv2.imshow("res ",image)
cv2.waitKey()