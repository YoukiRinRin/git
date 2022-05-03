import pygame
from pygame.locals import *
import sys

def main():
    pygame.init()
    #ウィンドウのサイズ
    screen = pygame.display.set_mode((600,500))
    #ウィンドウのタイトル
    pygame.display.set_caption("GAME")
    screen = pygame.display.set_mode
    font = pygame.font.Font(None,55)

    a = 0
    b = 0
    c = 0
    while(100):
        #背景の色
        
        screen.fill((a,b,c))
        text = font.render("TEST",True,(255,255,255))
        screen.blit(text,[20,100])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            a += 1
            b += 1
            c += 1

if __name__ == "__main__":
    main()