# background image and exit button
import tkinter as tk
from PIL import ImageTk, Image


root = tk.Tk()

root.title("PNG Viewer")
photo = tk.PhotoImage(file = "llama.png")
root.iconphoto(False, photo)

# get all the images
img0 = ImageTk.PhotoImage(Image.open("images\img0.png"))
img1 = ImageTk.PhotoImage(Image.open("images\img1.png"))
img2 = ImageTk.PhotoImage(Image.open("images\img2.png"))
img3 = ImageTk.PhotoImage(Image.open("images\img3.png"))
img4 = ImageTk.PhotoImage(Image.open("images\img4.png"))

img_list = [img0, img1, img2, img3, img4]

# status label
status = tk.Label(root, text="Image "+str(1)+" of "+str(len(img_list))+" ")
status["bd"] = 1
status["relief"] = tk.SUNKEN
status["anchor"] = tk.E
status.grid(row=2, column=0, columnspan=3, sticky=tk.E+tk.W)

# label
label = tk.Label(image=img0)
label.grid(row=0, column=0, columnspan=3)

# functions for buttons
def forward(n):
    global label
    global button_forward
    global button_quit
    
    label.grid_forget()
    label = tk.Label(image=img_list[n])
    label.grid(row=0, column=0, columnspan=3)

    status["text"]="Image "+str(n+1)+" of "+str(len(img_list))+" "
    status.grid(row=2, column=0, columnspan=3, sticky=tk.E+tk.W)
    
    button_back["command"]=lambda:back(n-1)
    button_forward["command"]=lambda: forward(n+1)

    if n <= 0:
        button_back["state"]=tk.DISABLED
    elif n >= 4:
        button_forward["state"]=tk.DISABLED
    else:
        button_forward["state"]=tk.NORMAL
        button_back["state"]=tk.NORMAL
    
    button_back.grid(row=1,column=0)
    button_quit.grid(row=1,column=1)
    button_forward.grid(row=1,column=2)
    return

def back(n):
    global label
    global button_forward
    global button_quit

    label.grid_forget()
    label = tk.Label(image=img_list[n])
    label.grid(row=0, column=0, columnspan=3)

    status["text"]="Image "+str(n+1)+" of "+str(len(img_list))+" "
    status.grid(row=2, column=0, columnspan=3, sticky=tk.E+tk.W)
    
    button_back["command"]=lambda:back(n-1)
    button_forward["command"]=lambda: forward(n+1)
    
    if n <= 0:
        button_back["state"]=tk.DISABLED
    elif n >= 4:
        button_forward["state"]=tk.DISABLED
    else:
        button_forward["state"]=tk.NORMAL
        button_back["state"]=tk.NORMAL
    
    button_back.grid(row=1,column=0)
    button_quit.grid(row=1,column=1)
    button_forward.grid(row=1,column=2)
    return

# create buttons
button_back = tk.Button(root, text = "<<", command=lambda: back(-1))
button_forward = tk.Button(root, text = ">>", command=lambda: forward(1))
button_quit = tk.Button(root, text = "Exit", command=root.destroy)

button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2, pady=5)

root.mainloop()
