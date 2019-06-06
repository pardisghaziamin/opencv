# Remove background of video

# purpose
the goal of this code is to remove a background of an image and all things that don't have any **change** or **movement**.

## First

Import libraries:

 -  we need **opencv**  for working with images
 - we need **numpy**  for working with arrays
  `import numpy`
 ` import cv2`

    
   

## Second

we read our video from camera using:

    cap=cv2.VideoCapture(0)
 
 

> "0" here means number of your camera you are using.

## Third

This line of code helps us to recognize all things that don't have any change:

    fg=cv2.createBackgroundSubtractorMOG2()
 
 ## Forth
 for saving your video you can use:
 

	fourcc=cv2.VideoWriter_fourcc(*'XVID')
	out=cv2.VideoWriter('output.avi', fourcc ,24.5,(640,480))
this means you are saving your video :

 - as a "avi" format 
 - via fourcc method
 - with 24.5 speed
 - and (640,480) size of frame


## Fifth

then,apply it on each frame of image.
    
	    while  True:
		_,frame=cap.read()
		fmask=fg.apply(frame)
		
		cv2.imshow('original',frame)
		cv2.imshow('fg',fmask)
		out.write(fmask)
    
 ## Result

> when you are working with videos,it needs to use this line end of your code.

    cap.release()


