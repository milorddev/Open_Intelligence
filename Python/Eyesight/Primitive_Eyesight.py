import cv2
import numpy as np
#from Tkinter import *
import os

WindowName = "Primitive Eyesight"
Room_Width = 500;
Room_Height = 400;


filename = "C:\OpenIntelligence\Open_Intelligence\ProjectFiles\IDE\Visual_Studio_2013\OpenIntelligence\OpenIntelligence\EyePrim_output.txt"


vc = cv2.VideoCapture(0)

PaintList = [];

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
    cv2.imshow('GreyScale',frame);


    greyframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
    b,g,r = cv2.split(frame)

    #sobelx = cv2.Sobel(greyframe,cv2.CV_64F,1,0,ksize=5)
    #sobely = cv2.Sobel(greyframe,cv2.CV_64F,0,1,ksize=5)
    
    #BlendSobel = cv2.addWeighted(sobelx,0.5,sobely,0.5,0);
    
    #edges = cv2.Canny(greyframe,61,161, apertureSize = 7)
    edges = cv2.Canny(greyframe, 75, 200)
    #lines = cv2.HoughLinesP(edges,1,np.pi/180,100,100,10)

    BlendFrame = cv2.addWeighted(greyframe,0.5,edges,0.5,0);

    

    for i in range(0,200):
        for j in range(0,200):
            PaintList = BlendFrame[i,j];
    
else:
    rval = False

readpic = greyframe

boundaries = [(100,200)];

IncrimentFrame = BlendFrame/BlendFrame
RoundFrame = BlendFrame/BlendFrame
Round2Frame = BlendFrame/BlendFrame

while(rval):
    rval, frame = vc.read()
    key = cv2.waitKey(20)

    if key == 27: # exit on ESC
        break 

    #frame = cv2.GaussianBlur(frame, (5, 5), 0)
    greyframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
    greyframe = cv2.GaussianBlur(greyframe, (5, 5), 0)

    
    #sobelx = cv2.Sobel(greyframe,cv2.CV_64F,1,0,ksize=5)
    #sobely = cv2.Sobel(greyframe,cv2.CV_64F,0,1,ksize=5)
    #BlendSobel = cv2.addWeighted(sobelx,0.5,sobely,0.5,0);

    edges = cv2.Canny(greyframe, 65, 65)
    #edges = cv2.Canny(greyframe,61,161, apertureSize = 7)

    #BlendFrame = cv2.addWeighted(greyframe,0.5,edges,0.5,0);

    edges.tofile(filename)

    
    ''' proof it works 
    f = open(filename, "rb")  # reopen the file
    f.seek(0, 0)  # seek
    x = np.fromfile(f,dtype=np.uint8)
    x = x.reshape(480,640)
    print x
    '''

    cv2.imshow('GreyScale',edges);

    
WriteFile = None
vc.release()
cv2.destroyAllWindows()

