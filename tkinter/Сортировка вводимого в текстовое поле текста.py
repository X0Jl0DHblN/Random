from tkinter import*
from tkinter import ttk

    
root = Tk()
root.geometry('400x300')


e = ttk.Entry(width = 20)
b = ttk.Button(text = 'Пуск')
l = ttk.Label(background = 'black', foreground = 'white')

def SortList(even):
    S = e.get()
    S = S.split()
    S.sort()
    l['text'] = ' '.join(S)
    
b.bind('<Button>', SortList)    

e.pack()
b.pack()
l.pack()

root.mainloop()
