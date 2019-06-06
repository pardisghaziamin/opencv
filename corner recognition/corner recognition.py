import numpy as np
import cv2

img1=cv2.imread('index.jpg')
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)

corners=cv2.goodFeaturesToTrack(gray,200,0.01,5)
corners=np.int0(corners)

for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img1,(x,y),3,(0,255,255),1)

cv2.imshow('corners',img1)
cv2.imwrite('img13.jpg',img1)
cv2.waitKey(0)
cv2.destroyAllWindows