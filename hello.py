"""
Created on Sat Dec 26 12:08:28 2020

@author: callia
"""
import tkinter as tk

root = tk.Tk()

for i in range(10):
    for j in range(10):
        mylabel = tk.Label(root, text = "p" + str(i) + str(j))
        mylabel.grid(row = i, column = j)

root.mainloop()
