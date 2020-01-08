import tkinter as tk
from PIL import Image, ImageTk

photo = None

master = tk.Tk()
buttons_frame = tk.Frame(master)
keys_frame = tk.Frame(master)
buttons_frame.pack()
keys_frame.pack()


def xiaoyu_pic():
    pil_image = Image.open(r"E:\个人资料文件\秘密花园\甜菜玉\图\mmexport1564498726843.jpg")
    if pil_image.size[0] > 500:
        width = 500
        height = int(pil_image.size[1] * (500 / pil_image.size[0]))
        pil_image = pil_image.resize((width, height), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(pil_image)
    return photo


# xiaoyu_pic1 = xiaoyu_pic()

btns_text = ("小玉", "Angela小热巴", "杨晨晨", "Carry陈良玲", "筱慧")
click_button_text = {
    "小玉": xiaoyu_pic,
    "Angela小热巴": "小热巴图",
    "杨晨晨": "杨晨晨",
    "Carry陈良玲": "Carry陈良玲",
    "筱慧": "筱慧"
}


def click_button(button_text):
    # print(click_button_text[button_text]())

    photo = click_button_text[button_text]()
    # print(type(photo))
    tp = tk.Toplevel(bg="yellow")
    tp.geometry("1200x900")
    frame_pic = tk.Frame(tp, width=800, height=600, bg="green")
    frame_pic.place(x=0, y=0)
    tp_label = tk.Label(frame_pic)
    tp_label.config(image=photo)
    tp_label.image = photo
    tp_label.place(x=0, y=0)


for button_text in btns_text:
    button1 = tk.Button(
        buttons_frame,
        text=button_text,
        command=lambda button_text=button_text: click_button(button_text))
    # print(button["text"].get())
    button1.pack(side="left", padx="10")
    # print(button1.getvar())
    type(button1["text"])

# for index in range(9):
#     button_text = btns_text[index]

#     button = Button(root, bg="White", text=button_text, width=5, height=1, relief=GROOVE,
#                     command=(lambda index=index, button_text=button_text: appear(index,button_text)))

# pass

for i in range(13):
    tk.Label(keys_frame,
             width="5",
             height="10",
             bg="black" if i % 2 == 0 else "white").pack(side="left", padx="1")

master.mainloop()
