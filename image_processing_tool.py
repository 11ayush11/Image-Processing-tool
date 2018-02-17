
#To import image and to work with ituse follwing code
from pylab import imread
image = imread('image path..')

#To plot image use
import matplotlib.pyplot as plt
plt.show()

#Now to know size of image
l,b,d = (image.shape)    ## l = length of image ,b = breadth of image, d = depth of image

#Now to reshape the image i.e. convert 3d image to 2d image
import numpy as np
reshaped_img = np.reshape(image,(l,b*d))   #This will convert 3d image to 2d image

#Now to resize image
import cv2
resize_image = cv2.resize(reshaped_img,(p,q))   # where p,q are new pixel value in which to want to reshape that 2d image i.e if p=100 &q=50 new image sie will be 100*50 pixels

#Lets convert this image into 1 dimensional image
b = resize_image.ravel()  #string of p*q 1dimensional columns each column having pixel value in string format

#Converting it to numerical format
X_data = np.asarray(b)                                        #asarray convert string to array format

##Now image is in 1 dimensional format can be used for preprocessing. 


