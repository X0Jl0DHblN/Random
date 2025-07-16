from tkinter import*
    
root = Tk()
root.geometry('500x300')
editor = Text()

charEditor = Text(height = 5, wrap = 'char')
charEditor.pack(anchor = N, fill = X)

wordEditor = Text(height = 5, wrap = 'word')
wordEditor.pack(anchor = S, fill = X)

root.mainloop()