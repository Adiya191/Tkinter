from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.title('Slider in Tk')
root.geometry("236x345")

def get_dollor():
    print(f"We have credited {myslider.get()} to your bank account")
    tmsg.showinfo("Amount Credited",f"We have credited {myslider.get()} dollor to your bank account")


#For Vertical
# myslider1 =Scale(root,from_=0,to=100)
# myslider1.pack()

Label(root,text='How many Dollor do you want?').pack()
myslider =Scale(root,from_=0,to=100,orient=HORIZONTAL)
#myslider.set(15)   #to set minimum number
myslider.pack()

Button(root,text="Get your Dollor Here...!",command=get_dollor).pack()







root.mainloop()