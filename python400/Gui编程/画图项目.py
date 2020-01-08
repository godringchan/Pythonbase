import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askyesno

win_width = 900
win_height = 450


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        # self.comands = {"1": self.test, "2": self.test2, "3": self.test3}
        # self.x = 0
        # self.y = 0
        self.fgcolor = "#ff0000"
        self.last_draw = 0
        self.startdraw = False
        self.bgcolor = "gray"
        self.createCanvas()
        self.createButtons()

    def createCanvas(self):  # 绘图部分
        self._canvas = tk.Canvas(self,
                                 width=win_width,
                                 height=win_height - 30,
                                 bg=self.bgcolor)
        self._canvas.pack()
        self._canvas.bind("<ButtonRelease-1>", self.stopdraw)

    def createButtons(self):
        button_names = ["开始", "画笔", "矩形", "清屏", "橡皮檫", "直线", "箭头",
                        "颜色"]  # 绘图按钮
        button_enames = [
            "start", "pencle", "rect", "clear", "erasor", "line", "lineArrow",
            "color"
        ]
        for i, v in enumerate(button_names):
            self.button = tk.Button(
                self,
                text=v,
                name=button_enames[i],
                width=10,
            )
            # command=lambda v=v: self.command_button(v))
            self.button.pack(side="left", padx=5, expand=tk.YES)
            self.button.bind_class("Button", "<1>", self.event_Manager)

    # def command_button(self, v):  # 按钮的功能
    #     def test1():
    #         print(f"我是{v}")

    #     def test2():
    #         print(f"我是{v}")

    #     def test3():
    #         print(f"我是{v}")

    #     commands = {
    #         "开始": test1,
    #         "画笔": test2,
    #         "矩形": test3,
    #         "清屏": test1,
    #         "橡皮檫": test1,
    #         "直线": test1,
    #         "箭头": test1,
    #         "颜色": test1
    #     }
    #     commands[v]()

    def event_Manager(self, event):
        name = event.widget.winfo_name()
        # print(name)
        if name == "line":
            # print("1")
            self._canvas.bind("<B1-Motion>", self.drawLine)
        elif name == "lineArrow":
            self._canvas.bind("<B1-Motion>", self.drawLineArrow)
        elif name == "rect":
            self._canvas.bind("<B1-Motion>", self.drawRect)
        elif name == "pencle":
            self._canvas.bind("<B1-Motion>", self.use_pencle)
        elif name == "erasor":
            # print("bind_erasor")
            self._canvas.bind("<B1-Motion>", self.use_erasor)
        elif name == "clear":
            self._canvas.delete("all")
        elif name == "color":

            self.fgcolor = askcolor(color=self.fgcolor)[1]

    def begindraw(self, event):
        self._canvas.delete(self.last_draw)
        if not self.startdraw:
            self.startdraw = True
            self.x = event.x
            self.y = event.y

    def stopdraw(self, event):
        self.startdraw = False
        self.last_draw = 0

    def use_pencle(self, event):
        self.begindraw(event)
        self._canvas.create_line(self.x,
                                 self.y,
                                 event.x,
                                 event.y,
                                 fill=self.fgcolor)
        self.x = event.x
        self.y = event.y

    def use_erasor(self, event):
        # print("use_erasor")
        self.begindraw(event)
        self._canvas.create_rectangle(event.x - 4,
                                      event.y - 4,
                                      event.x + 4,
                                      event.y + 4,
                                      fill=self.bgcolor,
                                      outline=self.bgcolor)
        self.x = event.x
        self.y = event.y

    def drawRect(self, event):
        self.begindraw(event)
        self.last_draw = self._canvas.create_rectangle(self.x,
                                                       self.y,
                                                       event.x,
                                                       event.y,
                                                       outline=self.fgcolor)

    def drawLineArrow(self, event):
        self.begindraw(event)
        self.last_draw = self._canvas.create_line(self.x,
                                                  self.y,
                                                  event.x,
                                                  event.y,
                                                  arrow=tk.LAST,
                                                  fill=self.fgcolor)

    def drawLine(self, event):
        self.begindraw(event)
        self.last_draw = self._canvas.create_line(self.x,
                                                  self.y,
                                                  event.x,
                                                  event.y,
                                                  fill=self.fgcolor)


def main():
    def callback():
        if askyesno("quit", "确定退出码"):
            root.destroy()

    root = tk.Tk()
    root.geometry(f"{win_width}x{win_height}+280+180")
    app = Application(root)
    # button_s = Button_s(root)
    app.pack()
    # button_s.pack()
    root.protocol("WM_DELETE_WINDOW", callback)
    root.mainloop()


if __name__ == "__main__":
    main()
