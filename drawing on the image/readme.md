# Drawing on the Image



## First

Import libraries:

 -  we need **opencv**  for working with images
 - we need **numpy**  for working with arrays
  `import numpy`
 ` import cv2`

    
   

## Second

we read our image file using:

    img=cv2.imread()

## Third

Then,we can draw a **line** on the image from one point to another.

`cv2.line(img,(100,200),(200,400),(0,255,0),10)`

 - first factor is the image that we want to draw on.
 -  second factor is first point
 - third factor is second point
 - forth factor is color
 - and fifth factor in width.

## Forth

we can draw a **rectangle** on the image using:

    cv2.rectangle(img,(100,200),(200,300),(0,0,255),5)


## Fifth

we can draw a **circle** on the image using:

    cv2.circle(img,(200,200),70,(0,0,255),5)

## Sixth

also we can draw a **polygonal** on the image which its points is introduced below:

    pts=np.array([[3,4],[5,6],[50 ,40],[30 ,70],[140,400],])
and

    cv2.polylines(img,[pts],False,(0,0,255),3)

	
> note: third factor is about closeness or openness,whenever polygonal is close,it will be **True** and likewise will be **False**.


## Seventh

we can **write**  on the image which its font is introduced below:

    font=cv2.FONT_HERSHEY_COMPLEX
 and
 

    cv2.putText(img,'hello',(100,100),font,1,(255,0,0),5)

# matplotlib

also we can use **matplotlib** to draw a line on the image.

    import matplotlib.pyplot as plt
after we import the library,then draw a line and show it.

    plt.imshow(img ,cmap='gray',interpolation='bicubic')

	plt.plot([200,300],[200,300],'r',linewidth=5)

	plt.show()

## End

we can use these lines of  code to whenever **q** button is pressed,the image will close. 

    if cv2.waitKey(1) & 0xFF == ord('q')
	    break

## Result
we can see the result here.

    cv2.imshow('frame',frame)
    
![enter image description here](https://lh3.googleusercontent.com/ix_lKQR58Vq3qTefw8U-Aag-8NYtS0eDD4qO1sDSfWOODXRtfsjWjns0RWnUKCl5sLP7BcN3kPM "g")

