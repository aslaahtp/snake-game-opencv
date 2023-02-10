from turtle import width
import cv2 as cv
import numpy as np
#blank image
#blank=np.zeros((500,500,3),dtype='uint8')
#1.paining entire screen with a color
#blank[200:300,200:300]=0,255,0
#cv.rectangle(blank,(0,0),(250,250),(0,255,0),cv.FILLED)
#cv.circle(blank,(250,250),40,(255,0,0),cv.FILLED)
#cv.line(blank,(0,0),(500,500),(0,0,255),thickness=2)
#2.writing text
#cv.putText(blank,'Hello',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,150,0),2)
#cv.imshow('frame',blank)
#cv.waitKey(0)
#

#basic functions in opencv
# 1.converting image to grayscale
#img=cv.imread('images/pizza.jpg')
#gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)
#cv.waitKey(0)
#

#2.blur
#img=cv.imread('images/pizza.jpg')
#blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)

#3.edge cascade
#canny=cv.Canny(blur,125,175)
#dilated image
#dilated=cv.dilate(canny,(7,7),iterations=3)

#contours 
#contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
#4.eroding
#eroded=cv.erode(dilated,(3,3),iterations=1)
#resize
#resized=cv.resize(eroded,(500,500),interpolation=cv.INTER_AREA)

#5.croping
#cropped=img[50:200,200:400]
#cv.imshow('Resized',cropped)
#cv.waitKey(0)
#

#image tranformation
 
#1.translation
#def translate(img,x,y):
#    transMat=np.float32([[1,0,x],[0,1,y]])
#    dimensions=(img.shape[1],img.shape[0])
#    return cv.warpAffine(img,transMat,dimensions)
    # -x-->left
    #  x-->right
    # -y-->up
    #  y-->down
#img=cv.imread('images/pizza.jpg')    
#translated=translate(img,200,200)

#2.rotation
#def rotate(img,angle,rotPoint=None):
#    (height,width)=img.shape[:2]
#    if rotPoint is None:
#        rotPoint=(width//2,height//2)
#    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0) 
#    dimensions=(width,height)
#    return cv.warpAffine(img,rotMat,dimensions)   
#rotated=rotate(img,45)        
#resize=cv.resize(rotated,(500,500))

#3.flip
#flip=cv.flip(img,0) 
#resize=cv.resize(flip,(500,500))
#cv.imshow('Flipped',resize)
#cv.waitKey(0)    
#
 


#image
#img=cv.imread('images/pizza.jpg')
#cv.imshow('burger',img)
#cv.waitKey(0)
#


#rescaling
#def rescaleFrame(frame,scale=0.75):
#    width=int(frame.shape[1]*scale)
#    height=int(frame.shape[0]*scale)
#    dimension=(width,height)
#    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
#    


#video
#capture=cv.VideoCapture('videos/hes.mp4')
#while True:
#    isTrue,frame=capture.read()
#    frame_resized=rescaleFrame(frame)
#    cv.imshow('vid',frame)
#    cv.imshow('Video',frame_resized)
#    if cv.waitKey(20) & 0xFF==ord('d'):
#        break
#capture.release()
#cv.destroyAllWindows()     