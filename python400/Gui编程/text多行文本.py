import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self._frame = tk.Frame(self.master)
        self.creadText()

    def creadText(self):
        self._text = tk.Text(self.master, width=40, height=12, bg="gray")

        button1 = tk.Button(self, text="输入了什么", command=self.textGet)
        button1.pack(side="left")
        self._text.pack()

    def textGet(self):
        self._text_get = self._text.get(1.0, tk.END)
        print(self._text_get, end="")


def main():
    master = tk.Tk(className="圣光小玉")
    master.title("小玉的圣光")
    master.geometry("300x400+500+500")
    app = Application(master)
    app.pack()
    master.mainloop()


if __name__ == "__main__":
    main()
