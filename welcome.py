# welcome
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Welcome")
photo = tk.PhotoImage(file = "llama.png")
root.iconphoto(False, photo)

bg = Image.open("green_red_bg.png")
resizedbg = ImageTk.PhotoImage(bg.resize((450, 600)))

canvas = tk.Canvas(root, width=450, height=600)
canvas.pack(fill="both", expand=True)

canvas.create_image(0, 0, image=resizedbg, anchor="nw")

fontmsg = canvas.create_text(225, 200, text="Sudoku",
                   font=("Helvetica", 50), fill = "white")
# entry
un_entry = tk.Entry(root, font=("Helvetica", 20), width=14, fg="salmon2")
un_entry.insert(0, "enter your name")
un_entry_window = canvas.create_window(225, 400, width=300, window=un_entry)

# helper function for button
def welcome():
    msg = "Welcome! " + un_entry.get()
    un_entry.destroy()
    start_btn.destroy()
    canvas.delete(fontmsg)

    canvas.create_text(225, 250, text=msg,
                       font=("Helvetica", 30), fill = "white")
    exit_btn = tk.Button(root, text="Exit", font=("Helvetica", 30), width=20,
                         fg="white", bg = "coral1", command=root.destroy)
    exit_btn_window = canvas.create_window(225, 500, width=200,
                                           window=exit_btn)
    
    
# button
start_btn = tk.Button(root, text="Start", font=("Helvetica", 30), width=20,
                      fg="white", bg="coral1", command=welcome)
start_btn_window = canvas.create_window(225, 500, width=200,
                                        window=start_btn)

# helper function for binding
def clear(e):
    if un_entry.get() == "enter your name":
        un_entry.delete(0, tk.END)
        # change text to stars
        # un_entry.config(show="*")
# bind the entry box
un_entry.bind("<Button-1>", clear)

root.mainloop()
