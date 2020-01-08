import PIL.Image as Img

pic_1 = Img.open(r"./pic/74940708_597084071101468_1743623235751749021_n.jpg")
pic_2 = Img.open(r"./pic/75516679_1427173930789067_1140612652205896611_n.jpg")

# 裁剪
pic_1_crop = pic_1.crop((150, 150, 555, 555))

#粘贴
pic_2.paste(pic_1_crop, (0, 0))
pic_2.show()