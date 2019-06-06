import numpy as np
import cv2

faceXML=cv2.CascadeClassifier('face.xml')
eyeXML=cv2.CascadeClassifier('eye.xml')

img=cv2.imread('face.jpg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=faceXML.detectMultiScale(gray)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),)
    roi_gray=gray[y:y+h,x:x+w]
    roi_img=img[y:y+h,x:x+w]
    eyes=eyeXML.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_img,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

cv2.imshow('img',img)
cv2.imwrite('img55.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows



