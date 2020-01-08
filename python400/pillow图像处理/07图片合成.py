from PIL import Image
from PIL import ImageChops

pic_1 = Image.open(r"./pic/74940708_597084071101468_1743623235751749021_n.jpg")
pic_2 = Image.open(
    r"./pic/75516679_1427173930789067_1140612652205896611_n.jpg")
# pic_1.show()

# 叠加
# ImageChops.add(pic_1, pic_2).show()

# 减法运算
# ImageChops.subtract(pic_1, pic_2).show()

# 使用darker函数,暗部变透明
# ImageChops.darker(pic_1, pic_2).show()

# 使用lighter函数,白色部分透明
# ImageChops.lighter(pic_1, pic_2).show()

# 两张图片相互叠加mulitpl
# ImageChops.multiply(pic_1, pic_2).show()

# screen()
# ImageChops.screen(pic_1, pic_2).show()

# 反色invert
# ImageChops.invert(pic_2).show()

# 差异函数difference
# ImageChops.difference(pic_1, pic_2).show()