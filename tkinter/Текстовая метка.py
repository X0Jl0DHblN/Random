from tkinter import*
from tkinter import ttk

root = Tk()
root.geometry('400x300')
label = ttk.Label(text = 'Привет, Паша!', font = ('Arial',30), borderwidth = 5,
                  relief = 'groove', padding = 10, background = '#3333DD', foreground = '#FFFFFF')
label.pack(expand = True)
root.mainloop()