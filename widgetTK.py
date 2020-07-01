from tkinter import *

root = Tk()
root.geometry("456x693")


def getvalue():
    print(f"The username is {uservalue.get()}")
    print(f"The password is {passvalue.get()}")


user = Label(root, text='username')
password = Label(root, text='password')
user.grid()  # pack
password.grid()  # pack

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(fg='red', text='Submit', command=getvalue).grid()

root.mainloop()
