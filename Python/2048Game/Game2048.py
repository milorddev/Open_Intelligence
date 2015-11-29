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

# create squares and attach values to it
VisibleSquare = [];
NumberValue = [];
spacing = 60;
for i in range(4):   
    for j in range(4):
        if random.randint(0,4) == 2:
           VisibleSquare.append(pygame.draw.rect(DISPLAYSURF, GREY, (0+(spacing*i), 0+(spacing*j), 50, 50)))
           NumberValue.append(2);
        else:
            VisibleSquare.append(0)
            NumberValue.append(0)

print VisibleSquare
print NumberValue




def PlayerMove():
    if OldMovement == KeyMovement:
        print "Same Move, Do Nothing!"
    else:
        print "Do it!"








while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            OldMovement = KeyMovement
            if event.key == pygame.K_LEFT:
                KeyMovement = "LEFT"
                print "LEFT"
            elif event.key == pygame.K_RIGHT:
                KeyMovement = "RIGHT"
                print "RIGHT"
            elif event.key == pygame.K_UP:
                KeyMovement = "UP"
                print "UP"
            elif event.key == pygame.K_DOWN:
                KeyMovement = "DOWN"
                print "DOWN"
            PlayerMove()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()



