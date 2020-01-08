import tkinter as tk
from tkinter.messagebox import showinfo, showerror

root = tk.Tk(className="找个美媚玩")
root.geometry("400x150+150+150")
frame_1 = tk.Frame(root)
frame_1.pack()

optionmenu_var = tk.StringVar()
optionmenu_var.set("你要找那位姑娘陪呢")
optionmenu_01 = tk.OptionMenu(frame_1, optionmenu_var, "杨晨晨", "小玉", "Carry陈良玲",
                              "刘亦宁", "小热巴")
# optionmenu_01["height"] = 25
optionmenu_01.pack()


def pri_optionmenu_var():
    print(optionmenu_var.get())
    showinfo(message=f"{optionmenu_var.get()}慢慢脱下了小内内，羞涩得脸颊泛红，下面的水都流出来了")
    showerror(message=f"{optionmenu_var.get()}把持不住，扑上来，脱掉了你的裤子，不断的亲了")


button_01 = tk.Button(frame_1, text="确定", command=pri_optionmenu_var)
button_01.pack()
root.mainloop()
