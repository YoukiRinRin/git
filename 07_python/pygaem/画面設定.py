import pygame
from pygame.locals import *
import sys

def main():
    #pygameの初期化
    pygame.init()
    #大きさ400*300の画面を生成
    screen = pygame.display.set_mode((400,300))
    pygame.display.set_caption("test")

    while(1):
        screen.fill((0,0,0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
if __name__ == "__main__":
    main()

