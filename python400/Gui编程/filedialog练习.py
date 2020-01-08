import tkinter as tk
from tkinter.filedialog import askopenfilenames
from PIL import Image, ImageTk

# fs = list()
flag = 0


def test01():

    # label_pic.quit()
    # root.mainloop()
    # f = askopenfilename(title="小玉在哪里呢",
    # initialdir=r"E:\个人资料文件",
    # filetypes=[("图片", "jpg")])
    # global fs
    fs1 = askopenfilenames(title="小玉在哪里呢",
                           initialdir=r"E:\个人资料文件",
                           filetypes=[("图片", "jpg")])
    # for i in fs1:
    #     fs.append(i)
    # sc.config(to=len(fs) - 1)
    # print(fs)
    frame_next_button = tk.Label(root)
    frame_next_button.pack()
    buttton_up = tk.Button(
        frame_next_button,
        text="上一张",
    )
    buttton_next = tk.Button(
        frame_next_button,
        text="下一张",
    )
    buttton_up.pack(side="left")
    buttton_next.pack(side="left")
    return (fs1, buttton_up, buttton_next)


def draw_pic(test01):
    fs2 = test01()
    len2 = len(fs2[0])
    try:
        root.update()
    finally:
        label_pic = tk.Label(root)

        def flag_add():
            global flag
            if flag < (len2 - 1):
                flag += 1
            # else:
            #     flag = flag
            # label_pic.config(image=tk_image)
            pil_image = Image.open(fs2[0][flag])
            if pil_image.size[0] > 300:
                width = 300
            else:
                width = pil_image[0]
            height = pil_image.size[1] * (width / pil_image.size[0])
            pil_image2 = pil_image.resize((int(width), int(height)),
                                          Image.ANTIALIAS)
            tk_image = ImageTk.PhotoImage(pil_image2)
            label_pic.config(image=tk_image)
            label_pic.image = tk_image

        def flag_pow():
            global flag
            if flag <= len2 and flag > 0:
                flag -= 1
            # label_pic.config(image=tk_image)
            pil_image = Image.open(fs2[0][flag])
            if pil_image.size[0] > 300:
                width = 300
            else:
                width = pil_image[0]
            height = pil_image.size[1] * (width / pil_image.size[0])
            pil_image2 = pil_image.resize((int(width), int(height)),
                                          Image.ANTIALIAS)
            tk_image = ImageTk.PhotoImage(pil_image2)
            label_pic.config(image=tk_image)
            label_pic.image = tk_image

        pil_image = Image.open(fs2[0][flag])
        if pil_image.size[0] > 300:
            width = 300
        else:
            width = pil_image[0]
        height = pil_image.size[1] * (width / pil_image.size[0])
        pil_image2 = pil_image.resize((int(width), int(height)),
                                      Image.ANTIALIAS)
        tk_image = ImageTk.PhotoImage(pil_image2)
        label_pic.config(image=tk_image)
        label_pic.image = tk_image
        # return label_pic.image

        fs2[1].config(command=flag_pow)
        fs2[2].config(command=flag_add)
        label_pic.pack()
        # frame_next_button.pack()


# def sc_command(value):
#     # sc = tk.Scale(root,
#     #               from_=0,
#     #               to=(len(fs)),
#     #               tickinterval=1,
#     #               orient=tk.HORIZONTAL,
#     #               command=sc_command)
#     text = fs[int(sc.get())]
#     label_pic_file.config(text=text)
#     print(text)
#     pil_img = Image.open(text)
#     if pil_img.size[0] > 300:
#         width = 300
#     else:
#         width = pil_img.size[0]
#     height = pil_img.size[1] * (300 / pil_img.size[0])
#     pil_img = pil_img.resize((int(width), int(height)), Image.ANTIALIAS)
#     tk_img = ImageTk.PhotoImage(pil_img)
#     label_pic.config(image=tk_img)
#     label_pic.image = tk_img  # 固定在内存中才能正常显示，不然会被主窗口重内存中清除
# label_pic["image"] = tk_img

# sc.config(to=len(fs))

# def flag_up
# print(f)
# print(len(fs))

# text = fs[sc.get()]
# label_pic_file.config(text=text)
# print(text)
# print(fs[sc.get()])

root = tk.Tk(className="和小玉做迷藏")
root.geometry("800x800+250+0")
button01 = tk.Button(root, text="快把小玉找出来", command=lambda: draw_pic(test01))
label_pic_file = tk.Label(root, text="小玉小玉")
# sc = tk.Scale(root,
#               from_=0,
#               to=(0),
#               tickinterval=1,
#               orient=tk.HORIZONTAL,
#               command=sc_command)
# label_pic = tk.Label(root)
# # frame_next_button = tk.Button(root)
# label_pic_file.pack()
button01.pack()
# sc.pack()
# label_pic.pack()
# frame_next_button.pack()
root.mainloop()
