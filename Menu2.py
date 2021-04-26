from future.backports.urllib.robotparser import Entry
from tkinter import *


def Tk():
    pass


top = Tk()

top.geometry("400x250")


class Label(object):
    pass


name = Label(top, text="Name").place(x=30, y=50)

email = Label(top, text="Email").place(x=30, y=90)

password = Label(top, text="Password").place(x=30, y=130)


class Button(object):
    pass


sbmitbtn = Button(top, text="Submit", activebackground="pink", activeforeground="blue").place(x=30, y=170)

e1 = Entry(top).place(x=80, y=50)

e2 = Entry(top).place(x=80, y=90)

e3 = Entry(top).place(x=95, y=130)

top.mainloop()  