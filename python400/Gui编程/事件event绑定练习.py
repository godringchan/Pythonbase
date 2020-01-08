import tkinter as tk

root = tk.Tk(className="和小玉一起画羞羞的画")
root.geometry("800x600+150+150")
c1 = tk.Canvas(root, width=200, height=200, bg="green")
c1.pack()


def mouse_test(event):
    print("鼠标相对位置{0}, {1}".format(event.x, event.y))
    print("鼠标绝对位置{0}, {1}".format(event.x_root, event.y_root))
    print("绑定的组件为{0}".format(event.widget))


def test_draw(event):
    c1.create_oval(event.x, event.y, event.x + 1, event.y + 1)


def key_press(event):
    print("按下了{0}键,code{1},char{2}".format(event.keysym, event.keycode,
                                           event.char))


c1.bind("<Button-1>", mouse_test)
c1.bind("<B1-Motion>", test_draw)

root.bind("<KeyPress>", key_press)

root.mainloop()
