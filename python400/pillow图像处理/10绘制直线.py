from PIL import Image, ImageDraw

pic_1 = Image.open(r"./pic/74940708_597084071101468_1743623235751749021_n.jpg")
w, h = pic_1.size
pic_draw = ImageDraw.Draw(pic_1)
pic_draw.line((0, 0, w, h), fill="red", width=7)
pic_draw.line((0, h, w, 0), fill="red", width=7)

pic_1.show()
