# trying to create button in Tkinter

import tkinter as tk

root = tk.Tk()

def click():
    mylabel = tk.Label(root, text = "You click a button!", fg = "dark green")
    mylabel.pack()

mybutton = tk.Button(root, text = "Click me!", command = click,
                     fg = "orange red2", bg = "sky blue", padx = 10, pady = 10)
mybutton.pack()

root.mainloop()
