from tkinter import*
    
root = Tk()
root.geometry('500x300')


editor = Text()
editor.pack(fill = BOTH, expand = 1)

editor.insert('1.0','Привет, Паша!')
editor.insert(END, '\n Конец')

root.mainloop()
