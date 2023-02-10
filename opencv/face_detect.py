import cv2 as cv
resize=cv.imread('images/face.jpg')
img=cv.resize(resize,[350,400])
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

haar_cascade=cv.CascadeClassifier('haar_face.xml')
faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
print(f'Number of faces={len(faces_rect)}')
for (x,y,w,h) in faces_rect:
    cv.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),thickness=2)
cv.imshow('Face',gray)    
cv.waitKey(0)