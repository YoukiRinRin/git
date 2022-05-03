import sys
import pygame
from pygame.locals import *

import os

Plyar1 =""
screen = pygame.display.set_mode((400,500))
str_title = "ジャンケンゲーム"


def show_screen():
    pygame.init()                                   # Pygameの初期化
    screen = pygame.display.set_mode((400, 300))    # 大きさ400*300の画面を生成
    pygame.display.set_caption("Test")              # タイトルバーに表示する文字

    while (1):
        screen.fill((0,0,0))        # 画面を黒色(#000000)に塗りつぶし
        pygame.display.update()     # 画面を更新
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()

def start():                                
    pygame.init()                                   # Pygameの初期化
    screen = pygame.display.set_mode((600, 600))    # 大きさ600*500の画面を生成
    pygame.display.set_caption("GAME")              # タイトルバーに表示する文字
    font = pygame.font.Font(None, 55)
                  
    while (1):
        screen.fill((0,0,0))                                    # 画面を黒色に塗りつぶし
        text = font.render("Game Start", True, (255,255,255))   # 描画する文字列の設定
        screen.blit(text, [20, 100])# 文字列の表示位置
        pygame.display.update()     # 画面を更新
        flg = 0
        # イベント処理
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
               flg = 1
               break
                
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()
        if flg == 1:
            break

def janken():
    pygame.init()                                   # Pygameの初期化
    screen = pygame.display.set_mode((600, 600))    # 大きさ600*500の画面を生成
    pygame.display.set_caption("GAME")              # タイトルバーに表示する文字
    font = pygame.font.Font(None, 55) 



    while (1):
        screen.fill((0,0,0))        
        img_gu = pygame.image.load("janken_gu.png")
        img_choki = pygame.image.load("janken_choki.png")
        img_pa = pygame.image.load("janken_pa.png")                                    # 画面を黒色に塗りつぶし
        #text = font.render("janken", True, (255,255,255))   # 描画する文字列の設定
        #screen.blit(text, [20, 100])# 文字列の表示位置
        screen.blit(img_gu, (20, 20))
        screen.blit(img_choki, (150,20))
        screen.blit(img_pa, (20, 170))


        pygame.display.update()     # 画面を更新
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()
            




def main():
    start()
    janken()
    


if __name__ == "__main__":
    main()

