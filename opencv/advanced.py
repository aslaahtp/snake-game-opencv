import cv2 as cv
from cv2 import rectangle
import numpy as np

img=cv.imread('images/pizza.jpg')
resize=cv.resize(img,(500,500),cv.ACCESS_WRITE)
blank=np.zeros(resize.shape[:2],dtype='uint8')
#color spaces
#a system for representing colors
#BGR to grayscale
#gray=cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
#BGR to hsv
#hsv=cv.cvtColor(resize,cv.COLOR_BGR2HSV)
#BGR to lab
#lab=cv.cvtColor(resize,cv.COLOR_BGR2LAB)
#

#color channnels
#b,g,r=cv.split(resize)
#blue=cv.merge([b,blank,blank])
#green=cv.merge([blank,g,blank])
#red=cv.merge([blank,blank,r])
#merging color channel
#merge=cv.merge([b,g,r])
#

#bluring
#averaging
#average=cv.blur(resize,(3,3))
#gausian blur
#gauss=cv.GaussianBlur(resize,(7,7),0)
#median blur
#median=cv.medianBlur(img,7)
#bilateral
#bilateral=cv.bilateral(img,10,35,25)
#

#bitwise operater
#pixel is turned off if value 0 and turned on if value 1
#rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
#circle=cv.circle(blank.copy(),(200,200),200,255,-1)   
#bitwise and
#bitwise_and=cv.bitwise_and(rectangle,circle)
#bitwise or
#bitwise_or=cv.bitwise_or(rectangle,circle)
#bitwise xor
#bitwise_xor=cv.bitwise_xor(rectangle,circle)
#bitwise not
#bitwise_not=cv.bitwise_not(circle)
#

#masking
mask=cv.circle(blank,(resize.shape[1]//2,resize.shape[0]//2),100,255,-1) 
masked=cv.bitwise_and(resize,resize,mask=mask)
cv.imshow('Mask image',masked)
cv.waitKey(0)