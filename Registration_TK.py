# registration form
from tkinter import *

root = Tk()
root.geometry("343x336")


def getvalue():
    print(
          f"{namevalue.get(), sexvalue.get(), agevalue.get(), contactvalue.get(), addressvalue.get(), agreevalue.get()}")

    with open("records.csv", 'a') as f:
        f.write(
            f"{namevalue.get(), sexvalue.get(), agevalue.get(), contactvalue.get(), addressvalue.get(), agreevalue.get()} \n")


name = Label(root, text='username')
name.grid()

sex = Label(root, text='Sex')
sex.grid()

age = Label(root, text='Age')
age.grid()

contact = Label(root, text='Contact No.')
contact.grid()

address = Label(root, text='Address')
address.grid()

namevalue = StringVar()
sexvalue = StringVar()
agevalue = StringVar()
contactvalue = StringVar()
addressvalue = StringVar()
agreevalue = IntVar()

nameentry = Entry(root, textvariable=namevalue)
sexentry = Entry(root, textvariable=sexvalue)
ageentry = Entry(root, textvariable=agevalue)
contactentry = Entry(root, textvariable=contactvalue)
addressentry = Entry(root, textvariable=addressvalue)

nameentry.grid(row=0, column=1)
sexentry.grid(row=1, column=1)
ageentry.grid(row=2, column=1)
contactentry.grid(row=3, column=1)
addressentry.grid(row=4, column=1)

agree = Checkbutton(text='agree the term & Condition', variable=agreevalue)
agree.grid(row=5, column=1)

Button(fg='blue', text='Form Submit', command=getvalue).grid(row=6, column=0)

root.mainloop()
