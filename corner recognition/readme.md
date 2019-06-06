# Corner recognition


## First

Import libraries:

 -  we need **opencv**  for working with images
 - we need **numpy**  for working with arrays
  `import numpy`
 ` import cv2`

    
   




## Second
read our images file and convert it to black and white:


    img=cv2.imread()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray=np.float32(img1gray)

 ## Third

we can find our desired feature on image using this code:

    corners=cv2.goodFeaturesToTrack(gray,200,0.1,50)
	corners=np.int0(corners)
 ## Forth
our recognition has finished,now it is time to make them separate using circle:
 

	for corner in corners:
		x,y=corner.ravel()
		cv2.circle(img1,(x,y),3,(0,255,255),1)


> note:
> "ravel" helps us to find a position(x,y) of each point that was recognized.

 ## Result
 ![](https://lh3.googleusercontent.com/h92PEVwXnblAN8QXgm5q2D0U5z8CoLufm5FK6woABxDX4tZL058Aplwv1KZWFSkSA87nHHc5F8Q "l")
![](https://lh3.googleusercontent.com/pnz3GoZkWNPZ8yejIK82ojH7y_ngm1UWxEgrTUMQHMPO0shcEnQKVgUOSzodBZ69bYzIzOVUaqY "j")



