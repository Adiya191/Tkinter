from tkinter import *

root=Tk()
root.title('Scroll Bar')
root.geometry("455x244")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

#insertion in the list box
# listbox = Listbox(root,yscrollcommand= scrollbar.set)
# for i in range(243):
#     listbox.insert(END,f'item{i}')
# listbox.pack(fill='both')
#scrollbar.config(command=listbox.yview)

#insertion in text
text=Text(root,yscrollcommand = scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)



root.mainloop()