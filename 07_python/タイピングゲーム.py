from tkinter import *
from tkinter import ttk
import random
import f_typing as type
root = Tk()
root.title('タイピングゲーム')
show_text=''

num_rand=0
inp_text=''




# ウィジェットの作成
frame1 = ttk.Frame(root, padding=16)

label1 = ttk.Label(frame1, text='上の文字を打ち込んでね')
lb_show = ttk.Label(frame1,text='')
t = StringVar()
entry1 = ttk.Entry(frame1, textvariable=t)


button1 = ttk.Button(
    frame1,
    text='OK',
    command= type.a())

# レイアウト
frame1.pack()
label1.pack(side=LEFT)
entry1.pack(side=LEFT)
button1.pack(side=LEFT)

# ウィンドウの表示開始
root.mainloop()
#def cheke_inp(inp_text,show_text):
#    if inp_text==show_text:
#        num_rand = random.randini(1,100)
#        lb_show
        
#        print('a')
