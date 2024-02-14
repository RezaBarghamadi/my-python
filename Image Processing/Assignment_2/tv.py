import numpy as np	
import cv2 
import imageio
image = cv2.imread("tr.jpg") 	
image = cv2.cvtColor (image , cv2.COLOR_BGR2GRAY)

rows, cols= image.shape
print(image.shape)
writer=cv2.VideoWriter("noise", cv2.VideoWriter_fourcc(*'mp4v'), 30, (cols, rows))

while True:
    image = cv2.imread("tr.jpg") 	
    image = cv2.cvtColor (image , cv2.COLOR_BGR2GRAY)
    noise=np.random.random((300 ,400))*255
    noise=np.array(noise,dtype=np.uint8)*1
    image[170:470, 200:600]=noise
    image= cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    writer.write(image)
    cv2.imshow('', image)
    if cv2.waitKey(25) & 0xFF==("q"):
            break
writer.release()
	
cv2.rectangle(image, (55, 215), (300, 28), 0, 1) 

imageio.mimsave('tv.gif', image, fps=60)