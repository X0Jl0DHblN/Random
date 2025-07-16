from tkinter import*

def finish():
    root.destroy()
    print('Осуществляется закрытие окна')
    
root = Tk()    
root.title('Первая программа')
root.geometry('400x300+400+200')
#root.resizable(True,False)
#root.minsize(200,100)
#root.maxsize(400,200)
root.protocol('Закрыть окно', finish)
Label()
l = Label(root,text = 'Привет!')
l.pack()
root.mainloop()
