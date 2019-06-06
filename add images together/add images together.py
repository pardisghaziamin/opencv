import numpy as np
import cv2
img=cv2.imread('city2.jpg')
img2=cv2.imread('trump.jpg')
#img3=img+img2
#img3=cv2.add(img,img2)
img3=cv2.addWeighted(img,0.7,img2,0.3,0)
cv2.imshow('img',img3)
cv2.waitKey(0)
cv2.destroyAllWindows
