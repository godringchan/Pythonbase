import PIL.Image as Img
import PIL.ImageEnhance as Enhance

pic_1 = Img.open(r"./pic/74940708_597084071101468_1743623235751749021_n.jpg")
pic_2 = Img.open(r"./pic/75516679_1427173930789067_1140612652205896611_n.jpg")

w, h = pic_1.size


# new_pic.show()
def pic_color_change():
    '''色彩调整'''
    '''创建比较图'''
    new_pic = Img.new("RGB", (w * 3, h))
    new_pic.paste(pic_1, (0, 0))
    ''''''
    img_color = Enhance.Color(pic_1)  # 获取色彩调整器
    pic_1_b = img_color.enhance(1.5)  # enhance的参数大于1为增强,小于1为减弱
    pic_1_c = img_color.enhance(0.7)  # 色彩减弱
    new_pic.paste(pic_1_b, (w, 0))
    new_pic.paste(pic_1_c, (w * 2, 0))
    new_pic.show()


def pic_brightness_change():
    '''亮度调整'''
    '''创建比较图'''
    new_pic = Img.new("RGB", (w * 3, h))
    img_brightness = Enhance.Brightness(pic_2)  # 获取亮度调整器
    pic_2_b = img_brightness.enhance(1.5)  # 亮度增强
    pic_2_c = img_brightness.enhance(0.7)  # 亮度减弱
    '''粘贴图片'''
    new_pic.paste(pic_2, (0, 0))
    new_pic.paste(pic_2_b, (w, 0))
    new_pic.paste(pic_2_c, (w * 2, 0))
    ''''''
    new_pic.show()


if __name__ == "__main__":
    pic_brightness_change()