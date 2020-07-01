#Gym registration form
from tkinter import *
root = Tk()
root.geometry("343x336")

def getvalue():
    print(f"The name of applicant is: {namevalue.get()}")
    print(f"The Age of the applicant is: {agevalue.get()}")
    print(f"The Address of the applicant is: {addressvalue.get()}")



name = Label(root,text='username')
name.grid()

age=Label(root,text='Age')
age.grid()

address=Label(root,text='Address')
address.grid()

namevalue = StringVar()
agevalue = StringVar()
addressvalue = StringVar()

nameentry=Entry(root,textvariable =namevalue)
ageentry=Entry(root,textvariable =agevalue)
addressentry = Entry(root,textvariable =addressvalue)

nameentry.grid(row=0,column=1)
ageentry.grid(row=1,column=1)
addressentry.grid(row=2,column=1)

Button(fg='blue',text='Form Submit',command=getvalue).grid()

root.mainloop()
