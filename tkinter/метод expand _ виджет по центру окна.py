from tkinter import*
from tkinter import ttk

root = Tk()
root.geometry('400x300')
btk = ttk.Button(text = 'Кнопка')
btk.pack(expand = True, anchor = SE)
root.mainloop()