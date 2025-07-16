from tkinter import *
from tkinter import ttk
    
root = Tk()
root.geometry('300x300')


editor = Text(height = 5)
editor.pack(anchor = N, fill = X)

label = ttk.Label()
label.pack(anchor = N, fill = BOTH)

def getText():
    label['text'] = editor.get('1.0', END)
    
button = ttk.Button(text = 'Нажми', command = getText) 

button.pack()

# =============================================================================
# def deleteText():
#     editor.delete('1.0', END)
#     
# button1 = ttk.Button(text = 'Clear', command = deleteText)    
# button1.pack()
# 
# =============================================================================
def replaceText():
    editor.replace('1.0', '1.10', 'Ура')
    
button2 = ttk.Button(text = 'Replace', command = replaceText)    
button2.pack()

root.mainloop()   
    

