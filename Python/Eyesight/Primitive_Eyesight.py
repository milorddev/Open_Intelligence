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


boundaries = [(100,200)];

IncrimentFrame = BlendFrame/BlendFrame
RoundFrame = BlendFrame/BlendFrame
Round2Frame = BlendFrame/BlendFrame

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
    
    #print BlendFrame[1,1];

    #mask = BlendFrame;
    
    
    
    for (lower, upper) in boundaries:
        lower = np.array(lower,dtype = "uint8")
        upper = np.array(upper,dtype = "uint8")

        mask = cv2.inRange(BlendFrame, lower, upper)

        IncrimentFrame += mask/7;
        IncrimentFrame *= mask/255;
        RoundFrame = np.around(IncrimentFrame,-2)
        RoundFrame *= 0.35;
        Round2Frame = np.around(RoundFrame,-2);
        Round2Frame *= 2;

        print Round2Frame[20,20]
       
    MixFrame = cv2.addWeighted(greyframe,0.5,Round2Frame,1,0);
    
    cv2.imshow(WindowName, BlendSobel)    
    cv2.imshow('GreyScale',mask);
    
   



        
    
vc.release()
cv2.destroyAllWindows()

