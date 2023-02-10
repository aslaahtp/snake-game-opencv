from ctypes import pointer
import cv2
import cvzone
import math
import random
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(3,1536)
cap.set(4,864)
from cvzone.HandTrackingModule import HandDetector
detector=HandDetector(detectionCon=0.8,maxHands=1)
class SnakeGameClass:
    def __init__(self,pathFood):
        self.points=[]
        self.lengths=[]
        self.currentLength=0
        self.allowedLength=150
        self.previousHead=0,0
        self.imgFood=cv2.imread(pathFood,cv2.IMREAD_UNCHANGED)
        (self.hFood,self.wFood)=self.imgFood.shape[:2]
        self.foodPoint=200,200
        self.score=0
        self.gameOver=False
        #randomFoodLocation()

    def randomFoodLocation(self):
        self.foodPoint=random.randint(100,1200),random.randint(100,600)    
    def update(self,imgMain,currentHead):
        if self.gameOver:
            cvzone.putTextRect(imgMain,"Game Over",[300,400],scale=7,thickness=5,offset=20)
            cvzone.putTextRect(imgMain,f'Your Score:{self.score}',[300,550],scale=7,thickness=5,offset=20)
        else:    
            px,py=self.previousHead
            cx,cy=currentHead 
            self.points.append([cx,cy])
            distance=math.hypot(cx-px,cy-py)
            self.lengths.append(distance) 
            self.currentLength+=distance  
            self.previousHead=cx,cy
            #length reduction
            if self.currentLength>self.allowedLength:
                for i,length in enumerate(self.lengths):
                    self.currentLength-=length
                    self.lengths.pop(i)
                    self.points.pop(i)
                    if self.currentLength<self.allowedLength:
                        break
            #check if snake ate the food
            rx,ry=self.foodPoint
            if rx-self.wFood//2<cx<rx+self.wFood//2 and ry-self.hFood//2<cy<ry+self.hFood//2:
                self.randomFoodLocation()
                self.allowedLength+=50 
                self.score+=1


            cvzone.putTextRect(imgMain,f'Your Score:{self.score}',[50,80],scale=2,thickness=3,offset=10)    
            #draw snake        
            if self.points:        
                for i,point in enumerate(self.points):
                    if i!=0:
                        cv2.line(imgMain,self.points[i-1],self.points[i],(0,0,255),20)
                cv2.circle(imgMain,self.points[-1],20,(200,0,200),cv2.FILLED)  
            #draw food
            rx,ry=self.foodPoint
            imgMain=cvzone.overlayPNG(imgMain,self.imgFood,(rx-self.wFood//2,ry-self.hFood//2))  
            #check for collision
            pts=np.array(self.points[:-2],np.int32)     
            pts=pts.reshape((-1,1,2))
            cv2.polylines(imgMain,[pts],False,(0,200,0),3)  
            minDist=cv2.pointPolygonTest(pts,(cx,cy),True) 
            if -1 <=minDist <= 1:
                self.gameOver=True
                self.points=[]
                self.lengths=[]
                self.currentLength=0
                self.allowedLength=150
                self.previousHead=0,0 
                self.randomFoodLocation()
        return imgMain    
game=SnakeGameClass('Donut.png')        
while True:
    success, frame = cap.read()
    frame=cv2.flip(frame,1)
    hands,frame=detector.findHands(frame,flipType=False)
    if hands:
        lmlist=hands[0]['lmList']
        pointIndex=lmlist[8][0:2]
        frame=game.update(frame,pointIndex)
    cv2.imshow('webcam', frame)
    key=cv2.waitKey(30)
    if key == ord('r'):
        game.score=0
        game.gameOver=False
    if (cv2.waitKey(30) == 27):
        break
