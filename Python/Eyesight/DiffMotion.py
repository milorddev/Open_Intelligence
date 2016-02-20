import cv2
import numpy as np


WindowName = "Primitive Eyesight"


cv2.namedWindow(WindowName)
vc = cv2.VideoCapture(0)


class Point:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;

class Rect:
    def __init__(self,topleft,bottomright):
        self.topleft = topleft;
        self.bottomright = bottomright;

RectList = [];
PointList = [];



# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0,255,(100,3))






if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
    empty, prevframe = vc.read()
    cv2.imshow(WindowName, frame)
    cv2.imshow('PreFrame',frame);

    DiffFrameDelta = frame*0
    

  
    
else:
    rval = False


while rval:
    prevframe = frame;
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

    DispFrame = frame.copy();
    
    #motion GET    
    GreyFrameCurrent = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
    GreyFramePrev = cv2.cvtColor(prevframe, cv2.COLOR_BGR2GRAY);

    GreyFrameCurrent = cv2.blur(GreyFrameCurrent,(5,5))
    GreyFramePrev = cv2.blur(GreyFramePrev,(5,5))
    
    
    #DiffFrame = cv2.absdiff(GreyFrameCurrent,GreyFramePrev)    

    #MotionData = cv2.threshold(DiffFrame, 25, 255, cv2.THRESH_BINARY)[1]



    # compute the absolute difference between the current frame and
    # first frame
    frameDelta = cv2.absdiff(GreyFramePrev, GreyFrameCurrent)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

    # dilate the thresholded image to fill in holes, then find contours
    # on thresholded image
    thresh = cv2.dilate(thresh, None, iterations=2)
    (_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #p1, st, err = cv2.calcOpticalFlowPyrLK(GreyFramePrev, GreyFrameCurrent, cnts, None, **lk_params)
    
    RectList = [];
    PointList = [];
    # loop over the contours
    for i,c in enumerate(cnts):
            
        # if the contour is too small, ignore i
        # compute the bounding box for the contour, draw it on the frame,
        # and update the text
        (x, y, w, h) = cv2.boundingRect(c)

        TopLeftPoint = Point(x,y);
        BottomRightPoint = Point(x + w, y + h);
        tempRect = Rect(TopLeftPoint, BottomRightPoint);
        tempPoint = Point(x+(w/2),y+(h/2));
        PointList.append(tempPoint)
        RectList.append(tempRect)

    tempPointList = [];
    for dum, f in enumerate(RectList):
        for num,k in enumerate(PointList):
            if dum == num:
                break;
            else:
                if k.x < RectList[dum].bottomright.x:
                    if k.x > RectList[dum].topleft.x:
                        if k.y < RectList[dum].bottomright.y:
                            if k.y > RectList[dum].topleft.y:
                                break;
                else:
                    tempPointList.append(k);

    PointList = tempPointList;
        
    #for i in RectList:
        #cv2.rectangle(DispFrame, (i.topleft.x,i.topleft.y), (i.bottomright.x,i.bottomright.y), (0, 255, 0), 2)

    for j in PointList:
        cv2.circle(DispFrame,(j.x,j.y),3,(0,255,0),-1);

        
    
    #BlendFrame = cv2.addWeighted(GreyFrameCurrent,0.5,MotionData,1,0)

  
    cv2.imshow(WindowName,DispFrame);
    cv2.imshow('PreFrame',frameDelta);

    



        
    
vc.release()
cv2.destroyAllWindows()

