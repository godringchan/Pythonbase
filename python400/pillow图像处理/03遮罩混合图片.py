import PIL.Image as Img

pic_1 = Img.open(r"./pic/74940708_597084071101468_1743623235751749021_n.jpg")
pic_2 = Img.open(r"./pic/75516679_1427173930789067_1140612652205896611_n.jpg")

r, g, b = pic_2.split()
Img.composite(pic_2, pic_1, g).show()
