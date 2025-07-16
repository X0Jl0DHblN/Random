from tkinter import*
from tkinter import ttk

def Entered(event):
    btn['text'] = 'Entered'
def Right(event):
    btn['text'] = 'Right'
    
root = Tk()
root.title('Обработчик событий ver.2')
root.geometry('400x300')
btn = ttk.Button(text = 'Click')
btn.pack(expand = True, anchor = N)
btn.bind('<Enter>', Entered)
btn.bind('<Leave>', Right)
root.mainloop()
