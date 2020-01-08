import PIL.Image as Img

pic_1 = Img.open(r"./pic/74940708_597084071101468_1743623235751749021_n.jpg")

# eval 调整像素亮度,(图像, 像素调整规则的函数)
# Img.eval(pic_1, lambda i: i * 0.5).show()

pic_2 = pic_1.copy()
pic_2.thumbnail((300, 400))
pic_2.show()