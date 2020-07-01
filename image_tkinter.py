from tkinter import *
from PIL import Image, ImageTk

image_root = Tk()

image_root.geometry("1255x954")


#image_insertion
image = Image.open("buddha.jpg")
photo = ImageTk.PhotoImage(image)

image_label = Label(image=photo)
image_label.pack()





image_root.mainloop()