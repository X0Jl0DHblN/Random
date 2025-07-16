from tkinter import*
from tkinter import ttk


        
def showMesage():
    x = int(e.get())
       
def showMesage1():
    symbol = e1.get()
    
def showMesage2():
    y = int(e2.get())
    
def result():
    a = int(e.get())
    b = int(e2.get())
    sym = e1.get()
    
    if sym == '+':
        res = a + b
    if sym == '-':
        res = a - b
    if sym == '*':
        res = a * b
    if sym == '/':
        res = a / b    
    l['text'] = int(res)
    
    
root = Tk()
root.geometry('400x300')

e = ttk.Entry()
e.pack(anchor = CENTER, padx = 10, pady = 10)

e1 = ttk.Entry()
e1.pack(anchor = CENTER, padx = 10, pady = 10)

e2 = ttk.Entry()
e2.pack(anchor = CENTER, padx = 10, pady = 10)

btn = ttk.Button(text = 'Посчитать', command = result)
btn.pack(anchor = CENTER, padx = 10, pady = 10)

l = ttk.Label()
l.pack(anchor = CENTER, padx = 10, pady = 10)

root.mainloop()