# Feature recognition

# Purpose:
the goal of this  code is to find a **similar features** between two images.
## First

Import libraries:

 -  we need **opencv**  for working with images
 - we need **numpy**  for working with arrays
 -  we need **matplotlib**  for draw any line on the image
  `import numpy`
 ` import cv2`
`from matplotlib import pyplot as plt`

 
    
   




## Second
read our images file :


    img=cv2.imread()
    
![enter image description here](https://lh3.googleusercontent.com/GUTjaWklKNVGyHRBsKXpbiXvOkjj6zC45ZI6SQCwS2Ow1ZyxkyD8wHL1y9nZ9TWQdCAjVNQnvVM "q")![enter image description here](https://lh3.googleusercontent.com/FTqM2kYRngKId0KYuX1OHfqrjKBDQ_AvomeYzl4dNbW4zqvj4sz9ExcgOf0NU4eoBFWw07YCT3E)
 ## Third

Define a detector with this line code:

    orb=cv2.ORB_create()
 ## Forth
Find the **key points** of each images :
 

	kp1,des1=orb.detectAndCompute(img1,None)
	kp2,des2=orb.detectAndCompute(img2,None)


## Fifth
now,compare **key points** of images which computed in last section and find the **matched features**. and find the detected **matched pointed**:

    bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
    matches=bf.match(des1,des2)
	matches=sorted(matches,key=lambda  x:x.distance)
## Sixth

you can show and connect detected **matched points** with these lines of code:

    img_out=cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=2)
	plt.imshow(img_out)
	plt.show()

 ## Result
![](https://lh3.googleusercontent.com/o4Wz48UagkoF3pwAoLvQZp4DxyoTJG0qAxc16OPn04qTssrasV5urbHFYyATdxkQbS6Z_o__lxY "u")

