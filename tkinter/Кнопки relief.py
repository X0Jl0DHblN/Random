from tkinter import*
from tkinter import ttk

root = Tk()
root.geometry('400x300')

B1 = Button(root, text ="FLAT", relief=FLAT )
B2 = Button(root, text ="RAISED", relief=RAISED )
B3 = Button(root, text ="SUNKEN", relief=SUNKEN )
B4 = Button(root, text ="GROOVE", relief=GROOVE )
B5 = Button(root, text ="RIDGE", relief=RIDGE )

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
root.mainloop()

