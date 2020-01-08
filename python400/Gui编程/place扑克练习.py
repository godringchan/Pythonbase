import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self.winfo_geometry()
        self.createWidget()

    def createWidget(self):
        # self.puke_photo = tk.PhotoImage(file=r"test_python_400\puke\puke1.gif")
        # self.puke1_label = tk.Label(self.master, image=self.puke_photo)
        # # self.puke1_label.pack()
        # self.puke1_label.place(x=10, y=10)
        self.puke_photos = [
            tk.PhotoImage(file=("test_python_400\\puke\\puke" + str(i + 1) +
                                ".gif")) for i in range(10)
        ]
        self.puke_photos_labels = [
            tk.Label(self.master, image=(self.puke_photos[i]))
            for i in range(10)
        ]
        for i in range(10):
            self.puke_photos_labels[i].place(x=10 + (i * 40), y=50)
        self.puke_photos_labels[0].bind_class("Label", "<Button-1>",
                                              self.chupai)

    def chupai(self, event):
        # print(event.widget.winfo_geometry())
        # print(event.widget.winfo_y())
        if event.widget.winfo_y() == 50:
            event.widget.place(y=30)
        else:
            event.widget.place(y=50)


def main():
    master = tk.Tk(className="与小玉玩嘿嘿嘿的游戏")
    # master.title = "与小玉玩游戏"
    master.geometry("800x600+150+150")
    app = Application(master=master)
    app.pack()
    master.mainloop()


if __name__ == "__main__":
    main()
