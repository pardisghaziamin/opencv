import numpy as np
import cv2

img=cv2.imread('hh.jpg')
laplacian=cv2.Laplacian(img,cv2.CV_8U)
sobelx=cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
sobely=cv2.Sobel(img,cv2.CV_8U,0,1,ksize=5)
canny=cv2.Canny(img,100,200)
cv2.imshow('img111',laplacian)
cv2.imshow('img11',canny)
cv2.imshow('img1',sobelx)
cv2.imshow('img',laplacian)
cv2.imwrite('laplacian.jpg',laplacian)
cv2.imwrite('canny.jpg',canny)
cv2.imwrite('sobelx.jpg',sobelx)
cv2.imwrite('sobely.jpg',sobely)
cv2.waitKey(0)
cv2.destroyAllWindows