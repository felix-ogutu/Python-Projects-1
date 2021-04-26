# import the tkinter
from tkinter import *
from functools import partial


# Function to perform the validation of the login
def validateLogin(Username, Password):
    print("username entered :", Username.get())
    print("password entered :", Password.get())
    return


loginWindow = Tk()
loginWindow.geometry('400x150')  # to create the size of the window
loginWindow.title('LOGIN SYSTEM')  # to create the name of the system
# username label and text entry
lblUsername = Label(loginWindow, text="Username").grid(row=0, column=0)
Username = StringVar()
etrUsername = Entry(loginWindow, textvariable=Username).grid(row=0, column=1)
# username label and text entry
lblPassword = Label(loginWindow, text="Password").grid(row=1, column=0)
Password = StringVar()
etrPassword = Entry(loginWindow, textvariable=Password, show='*').grid(row=1, column=1)
validateLogin = partial(validateLogin, Username, Password)

#login button
loginButton = Button(loginWindow, text="Login", command=validateLogin).grid(row=4, column=0)
loginWindow.mainloop()
