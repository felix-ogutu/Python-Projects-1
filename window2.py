import tkinter as tk

window = tk.Text()
label = tk.Label(text="Name")
entry = tk.Entry()
label.pack()
entry.pack()

label1 = tk.Label(text="Email Address")
entry1 = tk.Entry()
label1.pack()
entry1.pack()

label2 = tk.Label(text="Password")
entry2 = tk.Entry()
label2.pack()
entry2.pack()

label3 = tk.Label(text="Confirm the Password")
entry3 = tk.Entry()
label3.pack()
entry3.pack()
text_box = tk.Text()
text_box.pack()
window.mainloop()
