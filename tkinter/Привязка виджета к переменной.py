from tkinter import*
from tkinter import ttk

   
root = Tk()
root.geometry('400x300')

message = StringVar()

label = ttk.Label(textvariable = message)
label.pack(anchor = CENTER, padx = 10, pady = 10)

entry = ttk.Entry(textvariable = message)
entry.pack(anchor = CENTER, padx = 20, pady = 10)

btn = ttk.Button(textvariable = message)
btn.pack(anchor = N, padx = 5, pady = 10)

root.mainloop()
