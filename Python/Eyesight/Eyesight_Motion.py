import cv2
import numpy as np


WindowName = "Primitive Eyesight"
Room_Width = 500;
Room_Height = 400;


cv2.namedWindow(WindowName)
vc = cv2.VideoCapture(0)

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                 maxLevel = 2,
                 criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))


if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
    empty, prevframe = vc.read()
    cv2.imshow(WindowName, frame)
    cv2.imshow('PreFrame',frame);
    
    cv2.resizeWindow(WindowName,Room_Width,Room_Height);
    cv2.resizeWindow('PreFrame',Room_Width,Room_Height);


  
    
else:
    rval = False
color = np.random.randint(0,255,(100,3))
mask = np.zeros_like(frame)
RefFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);

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

    corners = cv2.goodFeaturesToTrack(RefFrame,25,0.01,10)
    OpticalFlow, st, err = cv2.calcOpticalFlowPyrLK(RefFrame, GreyFrameCurrent, corners, None, **lk_params)

    # Select good points
    good_new = OpticalFlow[st==1]
    good_old = corners[st==1]
    
    # draw the tracks
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
        frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
    img = cv2.add(frame,mask)

    # Now update the previous frame and previous points
    RefFrame = GreyFrameCurrent.copy()
    corners = good_new.reshape(-1,1,2)
        

    if not corners.any():
        print "Updating RefFrame";
        RefFrame = GreyFrameCurrent;
    else:
        for i in corners:
            x,y = i.ravel();
            cv2.circle(frame,(x,y),2,255,-1)


  
    cv2.imshow(WindowName,frame);
    cv2.imshow('PreFrame',DiffFrame);

    



        
    
vc.release()
cv2.destroyAllWindows()

