import tkinter as Tk
from tkinter import messagebox

root = Tk.Tk()
root.title("我的第一个GUI程序")
root.geometry("500x300+100+200")
btn_01 = Tk.Button(root)
btn_01["text"] = "点我就送花"
btn_01.pack()


def songhua(a):
    messagebox.showinfo("message", "送你一朵玫瑰花")


btn_01.bind("<Button-1>", songhua)


if __name__ == "__main__":
    root.mainloop()  # 进入事件循环
