import cv2
import numpy as np


WindowName = "Primitive Eyesight"
Room_Width = 500;
Room_Height = 400;


cv2.namedWindow(WindowName)
vc = cv2.VideoCapture(0)



if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
    empty, prevframe = vc.read()
    cv2.imshow(WindowName, frame)
    cv2.imshow('PreFrame',frame);
    
    cv2.resizeWindow(WindowName,Room_Width,Room_Height);
    cv2.resizeWindow('PreFrame',Room_Width,Room_Height);


  
    
else:
    rval = False




while rval:
    prevframe = frame;
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

    #motion GET    
    GreyFrameCurrent = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
    GreyFramePrev = cv2.cvtColor(prevframe, cv2.COLOR_BGR2GRAY);
    DiffFrame = cv2.absdiff(GreyFramePrev, GreyFrameCurrent)
    
    MotionData = cv2.threshold(DiffFrame, 25, 255, cv2.THRESH_BINARY)[1]
    
    BlendFrame = cv2.addWeighted(GreyFrameCurrent,0.5,MotionData,1,0);
  
    cv2.imshow(WindowName,frame);
    cv2.imshow('PreFrame',BlendFrame);

    



        
    
vc.release()
cv2.destroyAllWindows()

