import cv2

WindowName = "Primitive Eyesight"
Room_Width = 640;
Room_Height = 480;


cv2.namedWindow(WindowName)
vc = cv2.VideoCapture(0)


if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
    cv2.imshow(WindowName, frame)
    cv2.resizeWindow(WindowName,Room_Width,Room_Height);
else:
    rval = False



while rval:
    cv2.imshow(WindowName, frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

    frame = cv2.GaussianBlur(frame,(101,101),15)

    



    
vc.release()
cv2.destroyWindow(WindowName)

