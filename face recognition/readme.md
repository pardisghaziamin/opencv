# Face recognition

# purpose
Actually, in this code,we use **eye and face classifiers** which was
written before.
you can find it from:
[here
](https://github.com/opencv/opencv/tree/master/data/haarcascades)
## First

Import libraries:

 -  we need **opencv**  for working with images
 - we need **numpy**  for working with arrays
  `import numpy`
 ` import cv2`

    
   




## Second

Load the **classifier** files here:

    faceXML=cv2.CascadeClassifier('face.xml')
	eyeXML=cv2.CascadeClassifier('eye.xml')
 ## Third

read our images file and convert it to black and white:

    img=cv2.imread()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 ## Forth
 we can detect face with this line of code:
 

	faces=faceXML.detectMultiScale(gray)(640,480))



## Fifth

now,we are going to look for eyes on the each face that was detected in last section.
in faces:

 - draw a **blue rectangle** around the detected **face**.
 

	    for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),)

 and then,detect the eyes.
 

    roi_gray=gray[y:y+h,x:x+w]
	roi_img=img[y:y+h,x:x+w]
	eyes=eyeXML.detectMultiScale(roi_gray)

 
 - and around each detected **eyes**,draw a **red rectangle**.

    
	    for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_img,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    
 ## Result
![enter image description here](https://lh3.googleusercontent.com/O5XzdzhB4tmtanSTQTRtqHXbNnFKOtCxC4AlO05vx46M9FfrGWQL3VS4s9h3-uHPlslqp-ZzsyM "h")

