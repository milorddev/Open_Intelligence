import cv2
import numpy as np


WindowName = "Primitive Eyesight"
Room_Width = 500;
Room_Height = 400;


#cv2.namedWindow(WindowName)
vc = cv2.VideoCapture(0)



if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
    empty, prevframe = vc.read()
    cv2.imshow('Contours',frame);

    #cv2.resizeWindow('Contours',Room_Width,Room_Height);


  
    
else:
    rval = False




while rval:
    prevframe = frame;
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

    frame = cv2.medianBlur(frame,5)
    prevframe = cv2.medianBlur(prevframe,5)
    greyframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
    greyprevframe = cv2.cvtColor(prevframe,cv2.COLOR_BGR2GRAY);
    
    thresh1=cv2.adaptiveThreshold(greyframe,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    prevthresh = cv2.adaptiveThreshold(greyprevframe,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2);

    diffframe = (prevthresh + thresh1)/2;
    
    thresh2=cv2.adaptiveThreshold(diffframe,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    
    #im2, contours, hierarchy = cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE);

    #DispFrame = cv2.drawContours(frame, contours, -1, (0,255,0), 3)
  
    cv2.imshow('Contours',thresh1);
    cv2.imshow('Contours2',thresh2);


    



        
    
vc.release()
cv2.destroyAllWindows()

