# Edge detection

# Purpose:
the goal of this code is to detect a **edges** of images or videos.
## First

Import libraries:

 -  we need **opencv**  for working with images
 - we need **numpy**  for working with arrays
 
  `import numpy`
 ` import cv2`


 
    
   




## Second
read our image file :


    img=cv2.imread()
![enter image description here](https://lh3.googleusercontent.com/OzTYeEb8gA2QtwQIgmaVTo1esNihDHH_JDa-ijIcXe4PNkLg8gNeO14hNPGNE6cy_w1PTZmzDXQ "p")
 ## Third

There are many ways to detect edges of the image file:

 1. using **Laplacian** such as this:

	    laplacian=cv2.Laplacian(img,cv2.CV_8U)
![enter image description here](https://lh3.googleusercontent.com/ph17sJKLTlB-cJ2Q5ho5K83ZzletHnttIu-L9Q8Y7SHVPTnjIV4Ud6UjbO6OSRnugccJ0Kcczh8 "o")

 2. **Sobel** in **x** axis:

	 `sobelx=cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)`
	 
![enter image description here](https://lh3.googleusercontent.com/4MKD391DGNkP7yUEqX5zfqoSnXNxff1UTNua_muDvdQwZfal7r3G8s79UUX8IU2XqwMMfelIPr0 "ii")
 
 3. **Sobel** in **y** axis:

	 `sobely=cv2.Sobel(img,cv2.CV_8U,0,1,ksize=5)`
	 
![enter image description here](https://lh3.googleusercontent.com/7LMimJqH-9RYs1T9j4G5f3fv1LUyXh3YIH8KHffeKUteIaq5u9V_2RZVDQxxNRhx9nEYRxfyf5c "i")

 4. and **Canny**:

	    canny=cv2.Canny(img,100,200)
	    
![](https://lh3.googleusercontent.com/hWLSoAUEawyZbgU6LrJZUIXzm52w0r6jmNBmTpenPDodJME1_XXziQRei9qs2aQKdW9S5sO0yhc "y")
> note:
> as you see,**Canny** is the best way of all above.



