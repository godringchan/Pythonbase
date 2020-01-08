import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
from PIL import ImageTk, Image


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        # self.pack()
        self.createWdiget()

    def createWdiget(self):
        '''登录窗口'''
        self.label_01 = tk.Label(self, text="用户名")
        self.label_01.pack()
        self.u_name = tk.StringVar()
        self.entry01 = tk.Entry(self, textvariable=self.u_name)
        self.entry01.pack()
        self.u_name.set("小玉美美哒")
        self.label_02 = tk.Label(self, text="密码")
        self.label_02.pack()
        self.s_num = tk.StringVar()
        self.entry02 = tk.Entry(self, textvariable=self.s_num, show="*")
        self.entry02.pack()
        self.button_01 = tk.Button(self, text="确定", command=self.login)
        self.button_01.pack()

    def login(self):
        user_name = self.u_name.get()
        pwd = self.s_num.get()
        tkinter.messagebox.showinfo("人生苦短，我要小玉", f"{user_name}，想日小玉吗")
        if pwd == "love":
            y_or_n = tkinter.messagebox.askquestion("干不干", "相干就yes")
            # print(y_or_n)
            if y_or_n == "yes":
                file = tkinter.filedialog.askopenfilename()
                self.photo_pil = Image.open(file)

                # self.photo_pil.resize((170, 170))
                self.photo_tk = ImageTk.PhotoImage(self.photo_pil)
                # self.photo_tk.resize((self.ph))
                ch = int(self.photo_tk.height() / 5)
                cw = int(self.photo_tk.width() / 5)
                # print(ch)
                # print(cw)
                self.photo_tk = ImageTk.PhotoImage(
                    self.photo_pil.resize((ch, cw), Image.ANTIALIAS))
                # print(ch)
                # print(file1)
                self.t_window = tk.Toplevel()
                self.t_window.title("想就干啊")
                self.t_window.geometry(f"{cw}x{cw}+300+300")
                # self.t_frame = tk.Frame(self.t_window)
                # self.t_frame.pack()
                # self.photo = tk.PhotoImage(file=self.photo_tk)
                self.t_label = tk.Label(self.t_window)
                self.t_label["image"] = self.photo_tk
                # self.t_label.image = self.photo_tk
                # self.label.create_image(1,1,image=self.photo_tk)
                # self.label.pack(fill="both", expand=1)
                self.t_label.bind("<Configure>", self.changeSize)
                self.t_label.pack()

    def changeSize(self, event):
        w = self.t_label.winfo_width()
        # print(w)
        nw = event.width
        nh = int(event.height * (w / nw))
        self.photo_tk = ImageTk.PhotoImage(
            self.photo_pil.resize((nw, nh), Image.ANTIALIAS))
        self.t_label["image"] = self.photo_tk
        # self.t_label.image = self.photo_tk


def main():
    master = tk.Tk()
    master.title("想看小玉吗")
    # master.geometry("500x400+300+300")
    app = Application(master=master)
    # app2 = Application(master=master)
    app.pack()
    master.mainloop()


if __name__ == "__main__":
    main()
