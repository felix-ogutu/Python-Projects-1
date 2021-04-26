from tkinter import *
import random
import time
from time import strftime


# function to perform the function of the click of the calculator
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

    # This function is used to
    # display time on the label
    def time():
        string = strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000, time)

    # function to perform the action of declare


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

    # function to perform the function of equal sign of the calculator


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


root = Tk()
root.geometry("1600x800")
root.title("Restaurant Management System")
operator = ""
text_Input = StringVar()
Tops = Frame(root, width=1600, height=50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

F1 = Frame(root, width=800, height=700, bg="powder blue", relief=SUNKEN)
F1.pack(side=LEFT)

F2 = Frame(root, width=300, height=700, bg="powder blue", relief=SUNKEN)
F2.pack(side=RIGHT)

# the title information===============================
lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="Restaurant Management System", fg="Steel Blue", bd=10,
                anchor='w')
lblInfo.grid(row=0, column=0)

# code for the time======================================
# Styling the label widget so that clock
# will look more attractive
lbl = Label(Tops, font=('calibre', 30, 'bold'),
            background='purple',
            foreground='white', anchor='w')
lbl.grid(row=1, column=0)



# calculator===============================

textDisplay = Entry(F2, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                    bg="powder blue",
                    justify='right').grid(columnspan=4)

btn7 = Button(F2, padx=16, text="7", fg='black', bg='blue', command=lambda: btnClick(7),
              font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=1, column=0)
btn8 = Button(F2, padx=16, text="8", fg='black', bg='blue', command=lambda: btnClick(8),
              font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=1, column=1)
btn9 = Button(F2, padx=16, text="9", fg='black', bg='blue', command=lambda: btnClick(9),
              font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=1, column=2)
addition = Button(F2, padx=16, text="+", fg='black', bg='blue', command=lambda: btnClick("+"),
                  font=('arial', 20, 'bold'), height=1,
                  width=7).grid(
    row=1, column=3)
# ================================================================
btn4 = Button(F2, padx=16, text="4", fg='black', bg='blue', command=lambda: btnClick(4),
              font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=2, column=0)
btn5 = Button(F2, padx=16, text="5", fg='black', bg='blue', command=lambda: btnClick(5),
              font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=2, column=1)
btn6 = Button(F2, padx=16, text="6", fg='black', bg='blue', command=lambda: btnClick(6),
              font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=2, column=2)
subtraction = Button(F2, padx=16, text="-", fg='black', bg='blue', command=lambda: btnClick("-"),
                     font=('arial', 20, 'bold'), height=1,
                     width=7).grid(
    row=2, column=3)
# ===================================================================
btn1 = Button(F2, padx=16, text="1", fg='black', bg='blue', command=lambda: btnClick(1),
              font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=3, column=0)
btn2 = Button(F2, padx=16, text="2", fg='black', bg='blue', command=lambda: btnClick(2),
              font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=3, column=1)
btn3 = Button(F2, padx=16, text="3", fg='black', bg='blue', command=lambda: btnClick(3),
              font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=3, column=2)
multiplication = Button(F2, padx=16, text="*", fg='black', bg='blue', command=lambda: btnClick("*"),
                        font=('arial', 20, 'bold'), height=1,
                        width=7).grid(
    row=3, column=3)
# =========================================================
btn0 = Button(F2, padx=16, text="0", fg='black', bg='blue', command=lambda: btnClick(0),
              font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=4, column=0)
btnClear = Button(F2, padx=16, text="C", fg='black', bg='blue', command=btnClearDisplay,
                  font=('arial', 20, 'bold'), height=1,
                  width=7).grid(
    row=4, column=1)
btnEquals = Button(F2, padx=16, text="=", fg='black', bg='blue',
                   font=('arial', 20, 'bold'), height=1,
                   width=7, command=btnEqualsInput).grid(
    row=4, column=2)
division = Button(F2, padx=16, text="/", fg='black', bg='blue', command=lambda: btnClick("/"),
                  font=('arial', 20, 'bold'), height=1,
                  width=7).grid(
    row=4, column=3)

# ===================Others============================
# restraint menu
# Restraint Information 1
rand = StringVar()
lblReference = Label(F1, font=('arial', 16, 'bold'), text="Reference", bd=16, anchor='w')
lblReference.grid(row=0, column=0)
etrReference = Entry(F1, textvariable=rand).grid(row=0, column=1)
# information customer Data
customerData = StringVar()
lblCustomer = Label(F1, font=('arial', 16, 'bold'), text="Customer Data", bd=16, anchor='w')
lblCustomer.grid(row=1, column=0)
etrCustomer = Entry(F1, textvariable=rand).grid(row=1, column=1)

# Room allocation details
roomData = StringVar()
lblRoom = Label(F1, font=('arial', 16, 'bold'), text="Room Allocation", bd=16, anchor='w')
lblRoom.grid(row=2, column=0)
etrRoom = Entry(F1, textvariable=roomData).grid(row=2, column=1)
# Food expenses
foodData = StringVar()
lblFood = Label(F1, font=('arial', 16, 'bold'), text="Food Expenses", bd=16, anchor='w')
lblFood.grid(row=3, column=0)
etrFood = Entry(F1, textvariable=rand).grid(row=3, column=1)

root.mainloop()
