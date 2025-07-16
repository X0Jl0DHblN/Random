from tkinter import*
from tkinter import ttk

def clickButton():
    value = count.get()
    count.set(value + 1)
       
root = Tk()
root.geometry('400x300')

count = IntVar(value = 0)
button = ttk.Button(textvariable = count, command = clickButton)

button.pack()
root.mainloop()