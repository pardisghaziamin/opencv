print('hello')
import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('uu.jpg',cv2.IMREAD_GRAYSCALE)

pts=np.array([[3,4],[5,6],[50 ,40],[30 ,70],[140,400],])
cv2.polylines(img,[pts],False,(0,0,255),3)

font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'hello',(100,100),font,1,(255,255,0),5)

cv2.line(img,(100,200),(200,400),(0,255,0),10)

cv2.rectangle(img,(100,200),(200,300),(0,0,255),5)

cv2.circle(img,(200,200),70,(0,0,255),5)

plt.imshow(img ,cmap='gray',interpolation='bicubic')
plt.plot([200,300],[200,300],'r',linewidth=5)
plt.show()
cv2.imwrite('img.jpg',img)