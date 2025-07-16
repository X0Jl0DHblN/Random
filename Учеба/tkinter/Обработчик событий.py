
from tkinter import*
from tkinter import ttk

def Click():
    print('Привет, Паша!')
    
root = Tk()
root.title('Обработчик событий')
root.geometry('400x300')
btk = ttk.Button(text = 'Нажми', command = Click)
btk.pack(expand = True, anchor = N)
root.mainloop()
