from PIL import Image, ImageDraw

pic_1 = Image.open(r"./pic/74940708_597084071101468_1743623235751749021_n.jpg")

#创建画笔
pic_draw = ImageDraw.Draw(pic_1)
width, height = pic_1.size
pic_draw.arc((0, 0, width - 1, height - 1), 0, 360, fill="yellow")

pic_1.show()