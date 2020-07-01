#Aditya yadav
import urllib.request
from tkinter import *


def go():
    text.delete(1.0,END)
    with urlib.request.urlopen(entry.get()) as response:
        received_html = response.read()
    text.insert(1.0,received_html)

browser_window = Tk()
browser_window.title('Aadi Browser')
label =Label(browser_window,text='Enter URL:')
entry = Entry(browser_window)
entry.insert(END,'http://github.com')
button =Button(browser_window,text='GO',command=go)
text=Text(browser_window)
label.pack(side=TOP)
entry.pack(side=TOP)
button.pack(side=TOP)
text.pack(side=TOP)
browser_window.mainloop()
