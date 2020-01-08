import tkinter as tk


master = tk.Tk()
master.geometry("800x600")
frame_green = tk.Frame(master, bg="green", width=800, height=600)
frame_green.place(relx=0, rely=0)
tk.Button(master, text="小玉的美好肉体").place(x=50, y=100, width=200, height=50)
tk.Button(text="小玉的大奶子").place(x=40, y=80, width=200, height=50)
tk.Button(text="小玉的蜜桃臀").place(x=0, y=0, width=200, height=50)
tk.Button(frame_green, text="小玉的水蛇腰").place(relx=1, rely=1, x=-200, y=-50, width=200, height=50)
master.mainloop()