import pygame
from pygame.locals import *
import sys 

def main():
    (w,h) = (400,400)
    (x,z) = (w/2,h/2)
    pygame.init()
    pygame.display.set_mode((w,h),0,32) 
    screen = pygame.display.get_surface()
    pygame.display.set_caption("GAME")

    bg = pygame.image.load("S:\CARD-00006394.jpg").convert_alpha()
    rect_bg = bg.get_rect()

    player = pygame.image.load("S:\10226618i.jpg").convert_alpha()
    rect_player = player.get_rect()
    rect_player.center = (300,200)


    while(1):
        #screen.fill((0,0,0))
        #pygame.draw.line(screen,(0,95,0),(0,0),(80,80),5)
        #pygame.draw.rect(screen,(0,80,0),Rect(10,10,80,50),5)
        #pygame.draw.ellipse(screen,(0,100,0),(50,50,200,100),5)
        #pygame.display.update()


        pygame.display.update()
        pygame.time.wait(30)
        screen.fill((0,20,0,0))
        screen.blit(bg,rect_bg)
        screen.blit(player,rect_player)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
if __name__ == "__main__":
    main()