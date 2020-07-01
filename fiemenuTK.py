from tkinter import *

root=Tk()
root.geometry("683x373")
root.title("Menu Bar")

def myfunc():
    print("This is my Web App")

mainmenu =Menu(root)

m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label='New Project',command=myfunc)
m1.add_command(label='New ',command=myfunc)
m1.add_command(label='Open',command=myfunc)
m1.add_separator()
m1.add_command(label='Save',command=myfunc)
m1.add_command(label='Save As',command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='file',menu=m1)


m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label='Undo Backpace',command=myfunc)
m2.add_separator()
m2.add_command(label='Cut ',command=myfunc)
m2.add_command(label='Copy',command=myfunc)
m2.add_separator()
m2.add_command(label='Copy Reference',command=myfunc)
m2.add_command(label='Copy Path',command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='Edit',menu=m2)



root.mainloop()
