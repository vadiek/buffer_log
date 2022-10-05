
import pyperclip as pc
import keyboard as k
import tkinter as tk
import threading as th
from tkinter import scrolledtext
import time

def click():
    lab.configure(text='Начали')
    btn.configure(text='Остановить', command=stop)    
    t2.start()
    
    
def writer():
    try:
        while True:
            f = open('buffer.txt', 'a')
            k.wait("ctrl+v")
            print('1')
            x = pc.paste()
            f.write(x + '\n')
            f.close

    except KeyboardInterrupt:
        f.close


def stop():
    win.destroy()
    

#выше все функции используемые в проекте

#--------------------------------------------

win = tk.Tk()
win.geometry('400x250')

lab = tk.Label(win, text='Лог буфера обмена')
btn = tk.Button(win, text='Начать', command=click)

lab.grid(column=1, row=0)
btn.grid(column=1, row=1)

#создали окошко и настроили его параметры

#---------------------------------------------

t2 = th.Thread(target = writer)


