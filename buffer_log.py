import pyperclip as pc
import keyboard as k
import tkinter as tk

def main():
    lab.configure(text='Начали')
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


win = tk.Tk()
win.geometry('400x250')

lab = tk.Label(win, text='Лог буфера обмена')
btn = tk.Button(win, text='Начать', command=main)

lab.grid(column=2, row=2)
btn.grid(column=2, row=4)

win.mainloop()
