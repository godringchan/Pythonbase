from tkinter.colorchooser import askcolor
import tkinter as tk


def chooserColor_1():
    s1 = askcolor(color="red", title="小玉的幸运色")
    print(s1)
    # label01.config(bg=s1[1])
    label01["bg"] = s1[1]


root = tk.Tk(className="小玉喜欢的内内颜色")
root.geometry("800x600+150+70")
button_01 = tk.Button(root, text="为小玉选一个可爱的内内颜色吧", command=chooserColor_1)
button_01.pack()
label01 = tk.Label(root, width=250, height=250, bg="yellow")
label01.pack()
# print(label01.winfo_width())

root.mainloop()
