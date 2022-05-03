import requests
from bs4 import BeautifulSoup
from io import BytesIO
from tkinter import *
from tkinter import ttk

root = Tk()
root.minsize(width=250, height=150)
frame = ttk.Frame(root, padding=10)
frame.pack()
root.mainloop()


res = requests.get('https://www.ytv.co.jp/conan/trailer/index.html')

soup = BeautifulSoup(res.text,'html.parser')

figure = soup.figure

res_img = requests.get(figure.find('img')['src'])
#if res.status_code is 200:
#        i = BytesIO.Image.open(BytesIO(res_img.content))
#        i.save("a.jpg")

print(figure.find('img')['src'])
#print(soup.figure.contents)
#img_hint = soup.find_all('img')

