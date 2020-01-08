import tkinter as tk

root = tk.Tk()
root.geometry("800x600+150+150")


def test1(value):
    print("平滑变化", value)
    newFont = ("黑体", value)
    # print(la.getvar("length"))
    la.config(font=newFont)
    sc.config(font=newFont)
    sc.config(length=(int(value) * 11 + 200))
    print(sc.get())


sc = tk.Scale(root,
              bg="yellow",
              from_=10,
              to=50,
              length=200,
              tickinterval=5,
              orient=tk.HORIZONTAL,
              command=test1)
la = tk.Label(root, text="小玉水真多", width=200, height=50, bg="pink", fg="white")
sc.pack()
la.pack()

root.mainloop()
