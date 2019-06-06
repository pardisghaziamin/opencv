# Combination of images

we want to use a logo and add it into an another image.

## First

Import libraries:

 -  we need **opencv**  for working with images
 - we need **numpy**  for working with arrays
  `import numpy`
 ` import cv2`

    
   

## Second

we read our images file using:

    img=cv2.imread()
 
 ![](https://lh3.googleusercontent.com/aKBu5uyfhVQBnLhf7kwaGxhQe1LY55Nhza5qM5hbU2Auxq2qSavpXvlZ5d_yV5x2U83xuCvsRoI "kk")![](https://lh3.googleusercontent.com/aH4A650TjerhXKNehYfEPnb4LsoEaoMfjOJHj9TFquJC66M-z0BIUG88WCY9S60b-TUjo_5Sjds "ll")

## Third

we can extract the shape of the logo image:

    rows,cols,channels=img2.shape
 
## Forth

then,choose the part of the image that we want to add logo there.
    
    roi=img[0:rows,0:cols]
    
 ## Fifth

convert our image to black and white:

    img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
## Fifth

convert our image to black and white:

    img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
 ## Sixth

now we can convert image to **binary** ,which all pixel in rage 220-255 will be **1** and others will be **0**.


    ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY)
## Seventh
then,make it **reverse** using logical **NOT** operator and name it "mask"

    mask_inv=cv2.bitwise_not(mask)
## Eighth
now,prepare two form of image and then, add together.

 1. frontage
 2. background
 
**background**:
apply a logical **AND** between '"mask" and chosen part of image.

    img_bg=cv2.bitwise_and(roi,roi,mask=mask)

**frontage**:
apply a logical **AND** between inverted '"mask" and whole of the image.

    img2_fg=cv2.bitwise_and(img2,img2,mask=mask_inv)
    
 ## ninth
then,add **frontage** and **background** together and put it on chosen part.

    dst=cv2.add(img_bg,img2_fg)

	img[0:rows,0:cols]=dst
 
 
## Result
we can see the result here.

    cv2.imshow('img',img3)
    
![](https://lh3.googleusercontent.com/8fa773z2qXochyRmDn7zduMpaP8mXtOMLLrqE0dsJgnbb61_k4EoND7hpo-fSk6e9OvuhYGkgJA "k")

