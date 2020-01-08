import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfilename
from tkinter.messagebox import askyesno
from tkinter.colorchooser import askcolor


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self.open_file_read = None
        self.createMenuBar()
        self.createCascade()
        # 把菜单生成到主窗口中
        # self.master["menu"] = self.menubar
        self.text_pad()

    def createMenuBar(self):
        self.menubar = tk.Menu(self.master)

    def createCascade(self):
        # 创建子菜单
        menuFlie = tk.Menu(self.menubar)
        menuEdit = tk.Menu(self.menubar)
        MenuHelp = tk.Menu(self.menubar)
        # 把子菜单贴到菜单栏
        self.menubar.add_cascade(label="文件", menu=menuFlie)
        self.menubar.add_cascade(label="编辑", menu=menuEdit)
        self.menubar.add_cascade(label="帮助", menu=MenuHelp)
        # 为子菜单添加目录
        menuFlie.add_command(label="新建",
                             accelerator="ctrl+n",
                             command=self.new_file)
        menuFlie.add_command(label="打开",
                             accelerator="ctrl+o",
                             command=self.open_file)
        menuFlie.add_command(label="保存",
                             accelerator="ctrl+s",
                             command=self.save_file)
        menuFlie.add_command(label="另存为", command=self.test)
        menuFlie.add_separator()
        menuFlie.add_command(label="退出",
                             accelerator="ctrl+q",
                             command=self.quit_root)
        self.context_menu = tk.Menu(self.master)
        self.context_menu.add_command(label="改变背景色",
                                      command=self.chang_bg_Color)
        self.master.bind("<Button-3>", self.createContextmenu)

    def createContextmenu(self, event):
        # self.context_menu = tk.Menu(self.master)
        # self.context_menu.add_command(label="右键菜单", command=self.text)
        self.context_menu.post(event.x_root, event.y_root)

    def test(self):
        pass

    def chang_bg_Color(self):
        # askcolor()
        self.text__pad["bg"] = askcolor()[1]

    def new_file(self):
        # if askyesno(title="")
        title = "新建文件"
        if self.text__pad.get(1.0, tk.END) != "\n":
            if askyesno(title=f"确定{title}吗"):
                if askyesno(title="是否保存文件"):
                    file_name = asksaveasfilename(
                        title="文件保存为", initialfile="未命名.txt")  # TODO
                    with open(file_name, "w") as file:
                        file.write(self.text__pad.get(1.0, tk.END))
                    self.text__pad.delete(1.0, tk.END)
                else:
                    self.text__pad.delete(1.0, tk.END)

    def open_file(self):
        title = "打开新文件"
        if self.text__pad.get(1.0, tk.END) != "\n":
            if askyesno(title=f"确定{title}吗"):
                if askyesno(title="是否保存文件"):
                    file_name = asksaveasfilename(
                        title="文件保存为", initialfile="未命名.txt")  # TODO
                    with open(file_name, "w") as file:
                        file.write(self.text__pad.get(1.0, tk.END))
                    self.text__pad.delete(1.0, tk.END)
                else:
                    self.text__pad.delete(1.0, tk.END)
        with askopenfile() as f:
            self.open_file_name = f.name
            self.open_file_read = f.read()
            self.text_put()

    def save_file(self):
        try:
            with open(self.open_file_name, "w") as f:
                f.write(self.text__pad.get(1.0, tk.END))
        except AttributeError as e:
            asksaveasfilename(title="文件保存为")

    def quit_root(self):
        self.master.quit()

    def text_pad(self):
        self.text__pad = tk.Text(self, width=800, height=580, bg="gray")
        self.text__pad.pack()

    def text_get(self):
        self.text__get = self.text__pad.get(1.0, tk.END)
        # print(self.text__get)

    def text_put(self):
        # if self.text__pad.get(1.0, tk.END):
        self.text__pad.insert(1.0, self.open_file_read)


def main():
    root = tk.Tk()
    root.geometry("800x600+250+0")
    app = Application(master=root)
    root.config(menu=app.menubar)
    # button_test = tk.Button(text="调试按钮",
    #                         command=app.text_get)  # 用于调试方法的按钮，完成后注释掉
    # button_test.pack()  # 用于调试的按钮，完成后注释
    app.pack()
    # root.quit()
    root.mainloop()


if __name__ == "__main__":
    main()
