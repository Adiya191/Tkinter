from tkinter import *

root = Tk()
root.geometry("865x375")



frame=Frame(root,borderwidth=6,bg='grey',relief=SUNKEN)
frame.pack(side=TOP,anchor='sw')

b1 =  Button(frame,fg='red',text='Print Now')
b1.pack(side=LEFT,padx=44,pady=44)

b2 =  Button(frame,fg='black',text='I Agree')
b2.pack(side=LEFT,padx=44,pady=44)

b2 =  Button(frame,fg='blue',text='link here')
b2.pack(side=LEFT,padx=44,pady=44)

b2 =  Button(frame,fg='green',text='click here')
b2.pack(side=LEFT,padx=44,pady=44)

root.mainloop()
