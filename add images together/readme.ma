# Add images together



## First

Import libraries:

 -  we need **opencv**  for working with images
 - we need **numpy**  for working with arrays
  `import numpy`
 ` import cv2`

    
   

## Second

we read our images file using:

    img=cv2.imread()

## Third

There are three ways to add images together.

    img3=img+img2
if you use this code,your image will be bad-colored.

`img3=cv2.add(img,img2)`

and  the best way to do is:
 

    img3=cv2.addWeighted(img,0.7,img2,0.3,0)
    

> note:you can set how much of each image contain output image. 

## Result
we can see the result here.

    cv2.imshow('img',img3)
    
![enter image description here](https://lh3.googleusercontent.com/ix_lKQR58Vq3qTefw8U-Aag-8NYtS0eDD4qO1sDSfWOODXRtfsjWjns0RWnUKCl5sLP7BcN3kPM "g")

