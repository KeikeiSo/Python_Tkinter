# trying to get input in Tkinter

import tkinter as tk

root = tk.Tk()

e = tk.Entry(root, width = 50, borderwidth = 3)
e.pack()
e.insert(0, "Enter your name: ")

def welcome():
    warmwelcome = "Hello " + e.get() + "\nWelcome!"
    mylabel = tk.Label(root, text = warmwelcome, fg = "VioletRed1")
    mylabel.pack()

mybutton = tk.Button(root, text = "Click me!", command = welcome,
                     fg = "orange red2", bg = "sky blue", padx = 10, pady = 10)
mybutton.pack()

root.mainloop()
