import tkinter as tk
import tkinter.messagebox as ms
from PIL import ImageTk, Image


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self._frame = tk.Frame(self.master)
        self.creatRadioButton()
        self.print_bg_photo()
        # self.creatCheckButton()

    def creatCheckButton(self):
        def fack_xiaoyu():
            new_win.destroy()
            # print(self.upside)
            # print(self.upside.get())
            if self.upside.get():
                ms.showinfo("开干了", "推倒小玉，正面疯狂抽查")
            if self.blackside.get():
                ms.showinfo("开干了", "从后面进入了小玉身体，水流不停")
            if self._69side.get():
                ms.showinfo("开干了", "不断爱抚小玉，开启69模式")
            if self.rideside.get():
                ms.showinfo("开干了", "小玉坐了上来，不停扭动，爽得不要不要")
            yes_or_no = ms.askyesno("小玉高潮了几次", "小玉已经求饶了，射在里面吗")
            # print(yes_or_no)
            if yes_or_no:
                ms.showinfo("内射了小玉", "小玉再满足的抽搐，呻吟着")
            elif not yes_or_no:
                ms.showinfo("射到了小玉的嘴里", "小玉满足的舔着大鸡巴")

        ms.showinfo("小玉流了一地水", f"想{self.v.get()}小玉就{self.v.get()}啊")
        new_win = tk.Toplevel()
        new_win.geometry("400x26")
        self.upside = tk.IntVar()
        self.blackside = tk.IntVar()
        self._69side = tk.IntVar()
        self.rideside = tk.IntVar()
        self.c1 = tk.Checkbutton(new_win,
                                 text="正面刚",
                                 variable=self.upside,
                                 onvalue=1,
                                 offvalue=0)
        self.c2 = tk.Checkbutton(new_win,
                                 text="后入式",
                                 variable=self.blackside,
                                 onvalue=1,
                                 offvalue=0)
        self.c3 = tk.Checkbutton(new_win,
                                 text="69式",
                                 variable=self._69side,
                                 onvalue=1,
                                 offvalue=0)
        self.c4 = tk.Checkbutton(new_win,
                                 text="骑马式",
                                 variable=self.rideside,
                                 onvalue=1,
                                 offvalue=0)
        self.c1.pack(side="left")
        self.c2.pack(side="left")
        self.c3.pack(side="left")
        self.c4.pack(side="left")
        tk.Button(new_win, text="要用什么姿势",
                  command=fack_xiaoyu).pack(side="left")

    def creatRadioButton(self):
        def abc():
            ms.showinfo("小玉大腿已经张开", f"你选择了{self.v.get()}小玉")
            new_win.destroy()
            if self.v.get() == "干":
                self.creatCheckButton()
            # new_win.destroy()

        new_win = tk.Toplevel()
        new_win.geometry("200x24")
        self.v = tk.StringVar()
        self.v.set("干")
        self._radiobutton_1 = tk.Radiobutton(new_win,
                                             text="干",
                                             value="干",
                                             variable=self.v)
        self._radiobutton_2 = tk.Radiobutton(new_win,
                                             text="不干",
                                             value="不干",
                                             variable=self.v)
        self._radiobutton_1.pack(side="left")
        self._radiobutton_2.pack(side="left")
        tk.Button(new_win, text="确定", command=abc).pack(side="left")

    def print_bg_photo(self):
        pil_photo = Image.open(r"")
        if pil_photo.size[0] > 500:
            width = 500
            height = int(pil_photo.size[1] * (width / pil_photo.size[0]))
            a = pil_photo.resize((width, height), Image.ANTIALIAS)
            # self.photo = tk.PhotoImage(file=r"E:\个人资料文件\秘密花园\图片\Gif\006Bp6bbgy1fvnd4y3e16g306o06okan.gif")
            self.photo = ImageTk.PhotoImage(a)
            print("resize")
        else:
            self.photo = ImageTk.PhotoImage(pil_photo)
            print("noresize")
        print(pil_photo.size[0])
        self.photo_label = tk.Label(self, image=self.photo)
        self.photo_label.pack()


def main():
    master = tk.Tk(className="干小玉")
    master.geometry("800x600+300-100")
    app = Application(master=master)
    app.pack()
    master.mainloop()


if __name__ == "__main__":
    main()
