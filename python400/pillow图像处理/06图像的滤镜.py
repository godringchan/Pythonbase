from PIL import Image as Img
from PIL import ImageFilter

pic_1 = Img.open(r"./pic/74940708_597084071101468_1743623235751749021_n.jpg")
w = pic_1.width
h = pic_1.height
pic_new = Img.new("RGB", (w * 2, h))
pic_new.paste(pic_1, (0, 0))
# pic_new.show()
# pic_new.show()
# print(pic_new.size)
pic_2 = pic_1.filter(ImageFilter.GaussianBlur)
pic_new.paste(pic_2, (w, 0))
pic_new.show()
