import pygame
import sys
import random
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((640,480))
pygame.display.set_caption('2048')

# set up the colors
WHITE = (  255,   255,   255)
GREY = (200, 200, 200)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)

KeyMovement = "NONE";
OldMovement = "NONE";
SomethingHappened = True
xMult = 0;
yMult = 0;


# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 16)



class Square:
    def __init__(self, xLoc, yLoc, isTrue, value):
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.isTrue = isTrue
        self.value = value;
        self.label = myfont.render(str(self.value), 1, (255,255,0))
        self.rect = pygame.Rect(xLoc,yLoc,50,50)

        


# create squares and attach values to it
VisibleSquare = [];
NumberValue = [];
spacing = 60;
for i in range(4):   
    for j in range(4):
        if random.randint(0,4) == 2:
           VisibleSquare.append(Square(0+(spacing*i), 0+(spacing*j),True,2))
           #NumberValue.append(2);
           NumberValue.append("foosrowdah")
        else:
           VisibleSquare.append(Square(0+(spacing*i), 0+(spacing*j),False,0))
           NumberValue.append(0)

print VisibleSquare
print NumberValue






def PlayerMove():
        NoSpawn = False;
        for i,obj in enumerate(VisibleSquare):
            if VisibleSquare[i].isTrue:
                pygame.draw.rect(DISPLAYSURF, RED, (VisibleSquare[i].xLoc+25 + (50*xMult), VisibleSquare[i].yLoc+25 + (50*yMult), 5, 5))
                for j,sqr in enumerate(VisibleSquare):
                    if VisibleSquare[j].rect.collidepoint(VisibleSquare[i].xLoc+25 + (50*xMult), VisibleSquare[i].yLoc+25 + (50*yMult)):
                        if VisibleSquare[j].isTrue == False:
                            print "moving!"
                            VisibleSquare[j].isTrue = True;
                            VisibleSquare[j].value = VisibleSquare[i].value;
                            VisibleSquare[i].isTrue = False;
                            SomethingHappened = True
                            PlayerMove()
                        else:
                           if VisibleSquare[i].value == VisibleSquare[j].value:
                              print "Same val, changing!"
                              VisibleSquare[j].value += VisibleSquare[i].value
                              VisibleSquare[i].isTrue = False;
                              SomethingHappened = True
                           else:
                              print "Not same..."
                              SomethingHappened = False


                


def SpawnRandom():
    Selected = random.randint(0,15);
    if VisibleSquare[Selected].isTrue == False:
        VisibleSquare[Selected].value = 2;
        VisibleSquare[Selected].isTrue = True;
        print SomethingHappened;
    else:
        try:
            SpawnRandom();
        except RuntimeError:
            print "Game Over!"
            pygame.quit()
            sys.exit()
            
                
    





while True:
    for i,obj in enumerate(VisibleSquare):
        if VisibleSquare[i].isTrue == True:
            pygame.draw.rect(DISPLAYSURF, GREY, (VisibleSquare[i].xLoc, VisibleSquare[i].yLoc, 50, 50))
            VisibleSquare[i].label = myfont.render(str(VisibleSquare[i].value), 1, BLUE)
            DISPLAYSURF.blit(VisibleSquare[i].label, (15+ VisibleSquare[i].xLoc, 15+ VisibleSquare[i].yLoc))
        else:
            pygame.draw.rect(DISPLAYSURF, WHITE, (VisibleSquare[i].xLoc, VisibleSquare[i].yLoc, 50, 50))



    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            OldMovement = KeyMovement
            if event.key == pygame.K_LEFT:
                KeyMovement = "LEFT"
                xMult = -1;
                yMult = 0;
                print "LEFT"
            elif event.key == pygame.K_RIGHT:
                KeyMovement = "RIGHT"
                xMult = 1;
                yMult = 0;
                print "RIGHT"
            elif event.key == pygame.K_UP:
                KeyMovement = "UP"
                xMult = 0;
                yMult = -1;
                print "UP"
            elif event.key == pygame.K_DOWN:
                KeyMovement = "DOWN"
                xMult = 0;
                yMult = 1;
                print "DOWN"
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            PlayerMove()
            if KeyMovement != OldMovement:
                SpawnRandom()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()



