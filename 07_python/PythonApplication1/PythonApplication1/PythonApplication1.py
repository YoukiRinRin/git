
soup.a.text
soup.fing('a').text

soup.a.string
soup.find('a').string

soup('a')
soup,find_all('a')

soup('a').text
soup.find_all('a').text

soup.a.get('href')
soup.find('a').get('href')
[tag.get('href')for tag in soup('a')]

soup.find(class_='class_name')

soup(class = 'class_name')
soup.find_all(class_='class_name')

import requests

url = "https://www.sejuku.net/blog/"
response.encoding = response.apparent_encoding

print(response.text)

from bs4  import Beautifulsoupurl = "https://www.sejuku.net/blog/"

response = requests.get(url)
response.encoding = response.apparent_encoding

ba = Beautifulsoup(response.text,'html.parser')

for i in bs.select("h3"):
print(i.gettext)

for i in bs.select("h3"):
    print(i.gettext())

import sys
input = sys.stdin.readline

import heapq

class Heapq:
    def __init__(self,arrmdescending = False):
        self.sign = 1

        if descending:

            arr = [-a for a in arr]
            self.sign = -1

            self.hq = arr

            heapq.heapify(self.hq)

            def pop(self):
                return heapq.heapop(self.hq) * self.sign

            def pudh(self):
                return heapq.heappop(self.hq)*self.sign

            def push(self,a):
                heapq.heappush(self.hq,a*self.self.sign)

                def top(self):
                    return self.hq[0] * self.sign

            def can_pop

            import numpy
            
            N = int(input())
            X = list(map(int,input().split()))

            divisor_list = []
            for divisor in (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47):
                i = len(x) - 1
                flag = arg_path
                while i >= 0:
                    #print("--",X[i],divisor)
                    if X[i] % divisor == 0:
                    flag = True
                    X.pop(i)

                    i -= 1
                    if flag:
                        divisor_list.append(divisor)

                        print(numpy.prod(divisor_list))


def hangman(word):
    wrong = 0
    stages =["",
             "",
              "_______      ",
              "|            ",
              "|      |     ",
              "|      0     ",
              "|     /|\    ",
              "|     / \    ",
              "|            "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね！"
        char = input(msg)
        if char in rlettra:
            cind = rletters.index(char)
            boad[cind] = char
            rletters[cind] = '$'
            else:
                wrong += 1
                print(" ".join(board))
                w = wrong + 1
                print("\n".join(stages[0:e]))
                if "_" not in board:
                    print("あなたの勝ち！")
                    print(" ".join(board))
                    win = True
                    break
                if not win:
                    print("\n".join(stages[0:wrong+1]))
                    print("あなたの負け！正解は{}".format(word))
                    hangman("cat")
                    

import getpass
import re

if not win:
    print("\n".join(stages[0:wrong+1]))
    print("あなたの負け！正解は{}.".format(word))

    while True:
        player1 = "player1;英単語を入力してね（3文字以上6文字以内）"
        question = gatpass.getpass(player1)
        if not re.match('^[a-z]+$',question):
            print("英字で入力してね")
            else:
                if len(question) >= 3 and len(question) <= 6:
                    break
                else:
                    print("3文字以上6文字以内だよ！")

                    hangman(question)

while wrong < len(stages) -1
    print("\n")
    msg = "１文字"


pygame.display.uppdate()

while True:
    pygame.display.update()
    for event.type == QUIT:
        pygame.quit()
        sys.exit()

        color1 = pygame.Color(0,0,0)
        color2 = pygame.Color(255,255,255)
        color3 = pygame.Color(128,128,0)
        color1 = pygame.Color(0,0,0)