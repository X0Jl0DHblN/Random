

from tkinter import*
from tkinter import ttk

root = Tk()
root.geometry('400x300')
btk = ttk.Button(text = 'Нажми меня', state = ['disabled'])
btk.pack()
root.mainloop()