import cv2
import numpy as np
#next are using raspberry pi 3B serial
#import serial

cameraCapture = cv2.VideoCapture(1)
cv2.namedWindow('my win')
success,frame =  cameraCapture.read()

x=0
y=0
degree=0
distant=0
turn=0
ra=0
X1=0
X2=0
Y1=0
Y2=0

def circle(frame):

    global x
    global y
    global ra 
    circles = cv2.HoughCircles(frame,cv2.HOUGH_GRADIENT,1,120,param1=100,param2=30,minRadius=0,maxRadius=0)
    
    
    if circles is not None:
      circles = np.uint16(np.around(circles))
      for i in circles[0]:
      #choose the circle in the center of our camera vision
        if 420>i[0]>250 and i[2]>10 and i[1]<320:
          x=round(i[0])
          y=round(i[1])
          ra=round(i[2])          
    else :
      return 0

#return the slope of left black line of the track and distant from car to the track
def line(frame):
    edges=cv2.Canny(frame,50,120)
    minLineLength = 200
    maxLineGap = 15
    lines= cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
    global degree
    global distant
    global X1,X2,Y1,Y2
    Y3=0
    Y4=0
       

    if lines is not None:
     for x1,y1,x2,y2 in lines[0]:
      delta=x2-x1
      X1=x1
      X2=x2
      Y1=y1
      Y2=y2
      if 639>x1>60 and delta != 0 :   
       k=(y2-y1)/(x2-x1)
       degree=np.degrees(np.arctan(k))
       degree=round(degree)       
      if delta==0:
       degree=90
#only compute the distant when degree is 0.other times return 666 to stm32
    if (abs(Y1-Y2)) == 0 :
     if lines is not None:
      for i in range(len(lines)):
       for x1,y1,x2,y2 in lines[i]:
        if y1>Y4:
           Y4=y1
        if y2>Y3:
           Y3=y2
     distant=480-max(Y4,Y3)



#if found the most right side of the vision ,the tell the car to turn right 
def turnright(img):

    global turn
    avpix=0
    avpix2=0
    avpix1=0
    
    for i in img[370:476,637]:
      avpix1=avpix1+i
    avpix1=avpix1/110
    for j in img[370:476,638]:
      avpix2=avpix2+i
    avpix2=avpix2/110
    avpix=(avpix1+avpix2)/2
    if avpix < 80:
      turn=1
    

while success and cv2.waitKey(1)==-1:
    sdistant='000'
    sxy='000000'
    sdegree='000'
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray_img, 5)
    circle(img)
    line(img)
    turnright(img)

    if 90>=degree>80:
     degree=180-degree
     sdegree='0'+str(degree)
    if 80>=degree>0:
     degree=180-degree
     sdegree=str(degree)
    if  degree == 180 or degree == 0:
     sdegree='000'
    if degree == 366 :
     sdegree='366'
    if 0>degree>-10:
     degree=-(degree)
     sdegree='00'+str(degree)
    if -90<=degree<=-10:
     degree=-(degree)
     sdegree='0'+str(degree)
    if x>0:
      sxy=str(x)+str(y)
    else:
      sxy='000000'

    if 10<distant<100:
      sdistant='0'+str(distant)
    if 1<distant<10:
      sdistant='00'+str(distant)
    if distant>100:
      sdistant=str(distant)
    if distant==0:
      sdistant='000'
    
    
    #print to see if the data is correct
    #print('the distant  is:',sdistant[0:3])
    print(sxy[0:6]+sdegree[0:3]+sdistant[0:3]+str(turn))
    # send from rasberry Pi 3B to stm32 f409 when conneting with VNC 
    #dev.write((send[0:9] + str(distant)+str(turn)).encode())
    
    # draw the outer circle
    cv2.circle(frame,(x,y),ra,(0,255,0),2)    
    # draw the center of the circle
    cv2.circle(frame,(x,y),2,(0,0,255),3)
    #line
    cv2.line(frame,(X1,Y1),(X2,Y2),(255,0,0),2)
    
    cv2.imshow('my win',frame)
    x=0
    y=0
    distant=666
    degree=366
    turn=0
    success,frame =  cameraCapture.read()        
cameraCapture.release()    
