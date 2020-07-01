from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("683x373")
root.title("Tmsg Bar")

def myfunc():
    print("This is my Web App")
def help():
    print('i will help you')
    tmsg.showinfo("Help",'Aaadi will help you with this GUI')
def Rate_us():
    value = tmsg.askquestion('was your experience good','you have used this gui was your experience good?')
    print(value)
    if value == 'yes':
        print('please rete us on playstore ')
    else:
        print('sorry for inconvience...we will contact you soon')

 
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


m3 = Menu(mainmenu,tearoff=0)
m3.add_command(label='help',command=help)
m3.add_command(label='Rate',command=Rate_us)

root.config(menu=mainmenu)
mainmenu.add_cascade(label='Help',menu=m3)
root.mainloop()
