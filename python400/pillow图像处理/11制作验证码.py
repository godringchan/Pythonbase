import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont
width = 100
height = 100
# 创建一个新图片
new_pic = Image.new("RGB", (width, height), (255, 255, 255))
# 为新图片创建画笔
new_pic_draw = ImageDraw.Draw(new_pic)


# 获取颜色
def random_color():
    return (random.randint(200,
                           255), random.randint(200,
                                                255), random.randint(200, 255))


# 在新图片上每个点填上随机颜色
for x in range(width):
    for y in range(height):
        new_pic_draw.point((x, y), fill=random_color())


# 获取随机的4个字符
def random_chr():
    # return
    a = ""
    for i in range(4):
        a += chr(random.randint(65, 90))
    return a


# 利用变量把获取的随机字符保存起来
four_chrs = random_chr()

# 把字符填到新图片中
font = ImageFont.truetype("SIMLI.TTF", 36)
new_pic_draw.text((10, 50), font=font, text=four_chrs, fill=(255, 0, 0))

new_pic.show()