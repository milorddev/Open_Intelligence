import cv2
import numpy as np


WindowName = "Primitive Eyesight"
Room_Width = 500;
Room_Height = 400;


cv2.namedWindow(WindowName)
vc = cv2.VideoCapture(0)

PaintList = [];

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
    cv2.imshow(WindowName, frame)
    cv2.imshow('GreyScale',frame);
    
    cv2.resizeWindow(WindowName,Room_Width,Room_Height);
    cv2.resizeWindow('GreyScale',Room_Width,Room_Height);


    greyframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
    b,g,r = cv2.split(frame)

    #sobelx = cv2.Sobel(greyframe,cv2.CV_64F,1,0,ksize=5)
    #sobely = cv2.Sobel(greyframe,cv2.CV_64F,0,1,ksize=5)
    
    #BlendSobel = cv2.addWeighted(sobelx,0.5,sobely,0.5,0);
    
    edges = cv2.Canny(greyframe,61,161, apertureSize = 7)
    #lines = cv2.HoughLinesP(edges,1,np.pi/180,100,100,10)

    BlendFrame = cv2.addWeighted(greyframe,0.5,edges,0.5,0);

    

    for i in range(0,200):
        for j in range(0,200):
            PaintList = BlendFrame[i,j];
    
else:
    rval = False






while rval:
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

    greyframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
    b,g,r = cv2.split(frame)

    sobelx = cv2.Sobel(greyframe,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(greyframe,cv2.CV_64F,0,1,ksize=5)
    
    BlendSobel = cv2.addWeighted(sobelx,0.5,sobely,0.5,0);
    
    edges = cv2.Canny(greyframe,61,161, apertureSize = 7)
    #lines = cv2.HoughLinesP(edges,1,np.pi/180,100,100,10)

    #cv2.rectangle(frame,(0,0),(200,200),(212,212,212),3)

    BlendFrame = cv2.addWeighted(greyframe,0.5,edges,0.5,0);
    


    
    cv2.imshow(WindowName, BlendSobel)    
    cv2.imshow('GreyScale',BlendFrame);
    
   



        
    
vc.release()
cv2.destroyWindow(WindowName)
cv2.destroyWindow('GreyScale')

