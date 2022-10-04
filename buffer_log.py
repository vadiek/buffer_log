import pyperclip as pc
import keyboard as k


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
