import cv2

image=cv2.imread("bat.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
rows,cols=image.shape
_,image=cv2.threshold(image,100,255,cv2.THRESH_BINARY_INV)
cv2.putText(image,"My BATMAN ",(300,500),cv2.FONT_HERSHEY_SIMPLEX ,
            
            2,255,8)
cv2.imshow("res",image)
cv2.waitKey()
cv2.imwrite("batman.jpg",image)