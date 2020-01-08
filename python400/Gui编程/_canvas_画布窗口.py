import tkinter as tk
import random

class Appliaction(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self.createCanvas()
        self.create_Button()

    def createCanvas(self):
        self._canvas = tk.Canvas(self, width=400, height=300, bg="yellow")
        self._canvas.pack()
        line = self._canvas.create_line(10, 10, 30, 30)
        rect = self._canvas.create_rectangle(50, 50, 100, 100)
        oval = self._canvas.create_oval(50, 50, 100, 100)

    def create_Button(self):
        self.button_01 = tk.Button(self, text="画十个方形", command=self.draw_10_rects)
        self.button_01.pack(side="left")

    def draw_10_rects(self):
        # print(type(0, int(self._canvas["width"])))
        for i in range(10):
            x1 = random.randint(0, int(self._canvas["width"])//2)
            y1 = random.randint(0, int(self._canvas["height"])//2)
            x2 = x1 + random.randint(0, int(self._canvas["width"])//2)
            y2 = y1 + random.randint(0, int(self._canvas["height"])//2)
            self._canvas.create_rectangle(x1, y1, x2, y2)

def main():
    master = tk.Tk()
    master.geometry("800x600+100+100")
    app = Appliaction(master)
    app.pack()
    master.mainloop()


if __name__ == "__main__":
    main()