import cv2

import numpy as np 
image=np.ones((800,800))*255
#image =np.random.random((250,350))*255

#image=np.array(image,dtype=np.uint8)
#print (image)
cv2.rectangle(image,(30,130),(300,350),180,8)
cv2.circle(image,(20,3),80,120,8)
cv2.putText(image,"Reza Barghamadi",(30,300),cv2.FONT_HERSHEY_SIMPLEX ,
            
            2,0,8)
cv2.imshow("res",image)
cv2.waitKey()