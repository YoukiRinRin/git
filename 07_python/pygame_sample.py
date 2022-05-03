"""
import sys
import pygame
from pygame.locals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((500,657))
    (w,h) = (500,637)

    pygame.display.set_mode((w,h),0,32)
    screen = pygame.display.get_surface

    pygame.display.set_caption("pygame Test")
   

    while(True):
       screen.fill((0,0,0,0))
       pygame.time.wait(30)
       pygame.display.update
       
       for event in pygame.event.get():
         if event.type == QUIT:
             if event.key == K_ESCAPE:
                 pygame.quit()
                 sys.exit()


if __name__ == "__main__":
    main()
"""

import sys
import math
import pygame
from pygame.locals import *

WIDTH = 640
HEIGHT = 400
SIZE = 20
POS_X = 170
POS_Y = 310

pygame.init()

clock = pygame.time.Clock()
surface = pygame.display.set_mode((WIDTH,HEIGHT))

rect = pygame.Rect(POS_X,POS_Y,SIZE,SIZE)

angle = 0

pos_x = POS_X
pos_y = POS_Y

while True:
    for tmp in range(300-SIZE):

        surface.fill((0,0,0))

        rect.left = round(pos_x)
        rect.top = round(pos_y)

        pygame.dosplay.update()

        clock.tick(100)

        pos_x += math.cos(math.radians(angle))
        pos_y -= math.sin(math.radians(angle))


        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:

                pygame.quit()
                sys.exit()

    angle += 120
    if angle == 360:
        angle = 0


print("Hello")
