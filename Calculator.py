import tkinter as tk


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


window = tk.Tk()
window.title("Calculator")
operator = ""
text_Input = tk.StringVar()

textDisplay = tk.Entry(window, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                       bg="powder blue",
                       justify='right').grid(columnspan=4)

btn7 = tk.Button(window, padx=16, text="7", fg='black', bg='blue', command=lambda: btnClick(7),
                 font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=1, column=0)
btn8 = tk.Button(window, padx=16, text="8", fg='black', bg='blue', command=lambda: btnClick(8),
                 font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=1, column=1)
btn9 = tk.Button(window, padx=16, text="9", fg='black', bg='blue', command=lambda: btnClick(9),
                 font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=1, column=2)
addition = tk.Button(window, padx=16, text="+", fg='black', bg='blue', command=lambda: btnClick("+"),
                     font=('arial', 20, 'bold'), height=1,
                     width=7).grid(
    row=1, column=3)
# ================================================================
btn4 = tk.Button(window, padx=16, text="4", fg='black', bg='blue', command=lambda: btnClick(4),
                 font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=2, column=0)
btn5 = tk.Button(window, padx=16, text="5", fg='black', bg='blue', command=lambda: btnClick(5),
                 font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=2, column=1)
btn6 = tk.Button(window, padx=16, text="6", fg='black', bg='blue', command=lambda: btnClick(6),
                 font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=2, column=2)
subtraction = tk.Button(window, padx=16, text="-", fg='black', bg='blue', command=lambda: btnClick("-"),
                        font=('arial', 20, 'bold'), height=1,
                        width=7).grid(
    row=2, column=3)
# ===================================================================
btn1 = tk.Button(window, padx=16, text="1", fg='black', bg='blue', command=lambda: btnClick(1),
                 font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=3, column=0)
btn2 = tk.Button(window, padx=16, text="2", fg='black', bg='blue', command=lambda: btnClick(2),
                 font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=3, column=1)
btn3 = tk.Button(window, padx=16, text="3", fg='black', bg='blue', command=lambda: btnClick(3),
                 font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=3, column=2)
multiplication = tk.Button(window, padx=16, text="*", fg='black', bg='blue', command=lambda: btnClick("*"),
                           font=('arial', 20, 'bold'), height=1,
                           width=7).grid(
    row=3, column=3)
# =========================================================
btn0 = tk.Button(window, padx=16, text="0", fg='black', bg='blue', command=lambda: btnClick(0),
                 font=('arial', 20, 'bold'), height=1, width=7).grid(
    row=4, column=0)
btnClear = tk.Button(window, padx=16, text="C", fg='black', bg='blue', command=btnClearDisplay,
                     font=('arial', 20, 'bold'), height=1,
                     width=7).grid(
    row=4, column=1)
btnEquals = tk.Button(window, padx=16, text="=", fg='black', bg='blue',
                      font=('arial', 20, 'bold'), height=1,
                      width=7, command=btnEqualsInput).grid(
    row=4, column=2)
division = tk.Button(window, padx=16, text="/", fg='black', bg='blue', command=lambda: btnClick("/"),
                     font=('arial', 20, 'bold'), height=1,
                     width=7).grid(
    row=4, column=3)

window.mainloop()
