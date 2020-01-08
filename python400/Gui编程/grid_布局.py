import tkinter as tk
import tkinter.messagebox as ms


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self.createLogin()

    def createLogin(self):
        def click_enter():
            ms.showinfo("欢迎登录", f"用户名：{self.name_value.get()}\
                密码：{self.sn_value.get()}")

        def click_cancel():
            self.destroy()

        self.name_value = tk.StringVar()
        self.sn_value = tk.StringVar()
        self.name_label = tk.Label(self, text="姓名")
        self.name_label.grid(row=0, column=0, sticky="E")
        self.name_entry = tk.Entry(self, textvariable=self.name_value)
        self.name_entry.grid(row=0, column=1)
        self.phone_label = tk.Label(self, text="用户名为手机号")
        self.phone_label.grid(row=0, column=2)
        self.sn_label = tk.Label(self, text="密码")
        self.sn_label.grid(row=1, column=0)
        self.sn_entry = tk.Entry(self, textvariable=self.sn_value, show="*")
        self.sn_entry.grid(row=1, column=1)
        self._enter_button = tk.Button(self, text="登录", command=click_enter)
        self._enter_button.grid(row=2, column=1, sticky="EW")
        self._cancel_button = tk.Button(self, text="取消", command=click_cancel)
        self._cancel_button.grid(row=2, column=2, sticky="E")


def main():
    master = tk.Tk()
    # master.geometry("800x600+100+100")
    app = Application(master)
    app.pack()
    master.mainloop()


if __name__ == "__main__":
    main()