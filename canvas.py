import tkinter as tk

class Canvas(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.canvas = tk.Canvas(self, bg="white", height=500, width=440)
        self.canvas.pack()

    def draw_table(self):
        for i in range(1, 11):
            coord1 = 40, i*40, 400, i*40
            self.canvas.create_line(coord1, fill = "gray10")
            coord2 = i*40, 40, i*40, 400
            self.canvas.create_line(coord2, fill = "gray10")

""" main """
root = tk.Tk()
canvas = Canvas(master = root)
canvas.draw_table()
canvas.mainloop()
