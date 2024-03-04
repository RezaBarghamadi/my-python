import cv2

image=cv2.imread("reza.jpg")
image_g=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
face_detector=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
#location Facess

faces_location=face_detector.detectMultiScale(image_g,1.3)
for face in faces_location:
    x,y,w,h=face
    face=image[y:y+h, x:x+w]
    face_small=cv2.resize(face,[20,20])
    face_large=cv2.resize(face_small,[w,h],interpolation=cv2.INTER_NEAREST)
    image[y:y+h, x:x+w]=face_large
cv2.imshow("res ",image)
cv2.waitKey()
cv2.imwrite("chess_face.jpg",image)