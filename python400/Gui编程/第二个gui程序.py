"""测试一个经典的gui程序的写法，使用面向对象的方式"""

import tkinter as tk
from tkinter import messagebox


class Application(tk.Frame):
    """一个经典的gui程序的类的写法"""

    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建新的组件"""
        self.btn_01 = tk.Button(self)
        self.btn_01["text"] = "点击送花"
        self.btn_01.pack()
        self.btn_01["command"] = self.songhua
        self.btnQuit = tk.Button(self, text="退出", command=self.master.destroy)
        self.btnQuit.pack()

    def songhua(self):
        messagebox.showinfo("送花", "送你一朵玫瑰花")


def main():
    root = tk.Tk()
    root.geometry("400x300+500+300")
    root.title("一个类写法的gui")
    app = Application(master=root)
    app.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
