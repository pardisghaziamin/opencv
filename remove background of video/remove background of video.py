import numpy as np
import cv2

cap=cv2.VideoCapture(0)
fg=cv2.createBackgroundSubtractorMOG2()
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi', fourcc ,24.5,(640,480))

while True:
    _,frame=cap.read()
    fmask=fg.apply(frame)

    #cv2.imshow('ask',frame)
    #cv2.imshow('fg',fmask)
    out.write(fmask)

cv2.destroyAllWindows

cap.release()
out.release()
cv2.waitKey(0)