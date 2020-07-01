from tkinter import *
root = Tk()
root.geometry("567x567")
root.title("MY GUI")


title_label = Label(text ='''Probability theory is a mathematical framework for representing uncertain
statements. It provides a means of quantifying uncertainty and axioms for deriving
new uncertain statements. In artificial intelligence applications, we use probability
theory in two major ways. First, the laws of probability tell us how AI systems
should reason, so we design our algorithms to compute or approximate various
expressions derived using probability theory. Second, we can use probability and
statistics to theoretically analyze the behavior of proposed AI systems. ''',bg ='yellow',fg='black',padx =23,pady=84,font=('comicsansms',9,'bold'),borderwidth=4,relief=SUNKEN
)

title_label.pack(side=BOTTOM,fill =Y,anchor='se')





root.mainloop()