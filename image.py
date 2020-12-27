# background image and exit button
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

root.title("background")
photo = tk.PhotoImage(file = "llama.png")
root.iconphoto(False, photo)

img = ImageTk.PhotoImage(Image.open("green_red_bg.png"))
my_label = tk.Label(image = img)
my_label.pack()


button_quit = tk.Button(root, text = "Exit", command=root.destroy)
button_quit.pack()

root.mainloop()
