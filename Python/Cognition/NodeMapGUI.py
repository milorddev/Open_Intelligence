import cv2
import csv
import time
from random import randint

WindowName = "NodeMapGUI"


fpath = "C:\OpenIntelligence\Open_Intelligence\ProjectFiles\IDE\Visual_Studio_2013\OpenIntelligence\OpenIntelligence\GUICSV.csv"

with open(fpath,'r') as f:
    reader = csv.reader(f)
    NodeList = list(reader)


vc = cv2.VideoCapture(0)


if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
    frame *= 0;
    cv2.imshow(WindowName,frame);
    vc.release()

else:
    rval = False




class Bubble:
    def __init__(self,centerx,centery,size):
        self.centerx = centerx
        self.centery = centery
        self.size = size
        cv2.circle(frame,(centerx, centery),size,(255,255,255), -1)


    


for i,row in enumerate(NodeList):
    Bubble(randint(0,255),randint(0,255),30)
        




while(rval):
    key = cv2.waitKey(20)

    if key == 27: # exit on ESC
        break

    
    cv2.imshow(WindowName,frame)
    time.sleep(1)

    

cv2.destroyAllWindows()


'''
Cat
Dog,Cat,Animal
Animal
'''
