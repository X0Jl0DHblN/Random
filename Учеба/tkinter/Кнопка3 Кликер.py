from tkinter import *
from tkinter import ttk


count = 0
def clikcButton():
    global count
    count += 1
    btn['text'] = f'click{count}'
root = Tk()
root.geometry('300x200')
btn = ttk.Button(text = 'Нажми на кнопку', command = clikcButton)
btn.pack()
root.mainloop()