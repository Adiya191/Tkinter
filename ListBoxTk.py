from tkinter import *

root=Tk()
root.title('List Box')
root.geometry("456x234")


def add():
    global i
    lbx.insert(ACTIVE,f'{i}')
    i+=1
i=0
lbx=Listbox()
lbx.pack()
lbx.insert(END,'First item of our list')

Button(root,text='Add Item',command=add,).pack()


root.mainloop()