from tkinter import *

root=Tk()
root.geometry("456x234")
root.title("Status Bar")

def upload():
    statusvar.set('Busy.....')
    sbar.update()
    import time
    time.sleep(5)
    statusvar.set('Ready')


statusvar = StringVar()
statusvar.set('Start')
sbar = Label(root,textvariable=statusvar,relief=SUNKEN,anchor='w')
sbar.pack(side=BOTTOM,fill=X)

Button(root,text='Upload',command=upload).pack()



root.mainloop()
