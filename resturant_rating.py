#Resturant Rating


from tkinter import *
import tkinter.messagebox as tmsg


root = Tk()
root.title("Registration form")
root.geometry("543x336")


def get_review():
    print(f"We have rated {myslider.get()} Stars to our Resturant")
    tmsg.showinfo("Successfully Rated", f"We have rated {myslider.get()} Stars to our Resturant")

    print(
           f"{namevalue.get(), sexvalue.get(), agevalue.get(), contactvalue.get(), addressvalue.get(), myslider.get()}\n")

    with open("rated.csv", 'a') as f:
        f.write(
                 f"{namevalue.get(), sexvalue.get(), agevalue.get(), contactvalue.get(), addressvalue.get(), myslider.get()} \n")

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

Label(root, text='How many Star you like to give?').grid()
myslider = Scale(root, from_=0, to=10, orient=HORIZONTAL)
# myslider.set(15)   #to set minimum number
myslider.grid()

Button(root, text="Rate Here!", command=get_review).grid()



root.mainloop()
