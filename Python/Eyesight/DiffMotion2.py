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

        # setup initial location of window
        r,h,c,w = 250,90,400,125  # simply hardcoded the values
        track_window = (c,r,w,h)

        # set up the ROI for tracking
        roi = DispFrame[r:r+h, c:c+w]
        hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
        roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
        cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

        # Setup the termination criteria, either 10 iteration or move by atleast 1 pt
        term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

        hsv = cv2.cvtColor(DispFrame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

        # apply meanshift to get the new location
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)

        # Draw it on image
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv2.polylines(DispFrame,[pts],True, 255,2)

        

        TopLeftPoint = Point(x,y);
        BottomRightPoint = Point(x + w, y + h);
        tempRect = Rect(TopLeftPoint, BottomRightPoint);
        tempPoint = Point(x+(w/2),y+(h/2));
        PointList.append(tempPoint)
        RectList.append(tempRect)

       
        
    #for i in RectList:
        #cv2.rectangle(DispFrame, (i.topleft.x,i.topleft.y), (i.bottomright.x,i.bottomright.y), (0, 255, 0), 2)

    for j in PointList:
        cv2.circle(DispFrame,(j.x,j.y),3,(0,255,0),-1);

        
    
    #BlendFrame = cv2.addWeighted(GreyFrameCurrent,0.5,MotionData,1,0)

  
    cv2.imshow(WindowName,DispFrame);
    cv2.imshow('PreFrame',frameDelta);

    



        
    
vc.release()
cv2.destroyAllWindows()

