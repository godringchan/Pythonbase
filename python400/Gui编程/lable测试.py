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
        self.creatlabel()

    def createWidget(self):
        """创建新的组件"""
        self.btn_01 = tk.Button(self)
        self.btn_01["text"] = "点击送花"
        self.btn_01.pack()
        self.btn_01["command"] = self.songhua
        self.btnQuit = tk.Button(self, text="退出", command=self.master.destroy)
        self.btnQuit.pack()
        self.btn_02 = tk.Button(self,
                                text="点击打开小玉",
                                command=self.call_new_window)
        self.btn_02.pack()

    def creatlabel(self):
        self.lablel = tk.Label(
            self,
            text="label的测试",
            width=10,
            height=2,
            bg="black",
            fg="yellow",
        )
        self.lablel.pack()

        self.lablel2 = tk.Label(self,
                                text="多个label的测试",
                                width=15,
                                height=2,
                                bg="green",
                                fg="red",
                                font=("雅黑", 30))
        self.lablel2.pack()
        # 显示图像
        # global photo
        # self.photo = tk.PhotoImage(file=r"E:\个人资料文件\秘密花园\图片\Gif\006Bp6bbgy1fvnd4y3e16g306o06okan.gif")
        # self.lablel3 = tk.Label(self, image=self.photo)
        # self.lablel3.pack()
        self.lablel4 = tk.Label(self,
                                text="小玉真漂亮\n胸又大\n性格好\n还很骚",
                                borderwidth=5,
                                relief="groove",
                                justify="left",
                                font=("雅黑", 30))
        self.lablel4.pack()

    def songhua(self):
        messagebox.showinfo("送花", "送你一朵玫瑰花")

    def call_new_window(self):
        new_root = tk.Toplevel()
        new_root.geometry("400x600+500+50")
        new_frame = tk.Frame(new_root)
        new_frame.pack()

        self.photo = tk.PhotoImage(
            file=r"E:\个人资料文件\秘密花园\图片\Gif\006Bp6bbgy1fvnd4y3e16g306o06okan.gif")
        new_lable1 = tk.Label(new_frame, image=self.photo)
        new_lable1.pack()
        button_1 = tk.Button(new_frame, text="新窗口")
        button_1.pack()


def main():
    root = tk.Tk()
    root.geometry("400x600+500+50")
    root.title("lable测试")
    app = Application(master=root)
    app.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
