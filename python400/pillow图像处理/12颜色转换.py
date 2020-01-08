import PIL.Image as Img
import PIL.ImageDraw as Imgd

pic_1 = Img.open(r"./pic/75516679_1427173930789067_1140612652205896611_n.jpg")
# 获取图片的高,宽
width, height = pic_1.size
# 生成图片的画笔
pic_1_draw = Imgd.Draw(pic_1)


# 得到新颜色的方法
def new_color(old_color):
    if old_color[0] > 60 and old_color[1] > 60:
        return (old_color[0], 0, old_color[2])


# 改变图片的颜色, 获取每个点的坐标开始
for x in range(width):
    for y in range(height):
        # 获取每个点像素的颜色
        old_color = pic_1.getpixel((x, y))
        # 对点的颜色进行重新填充
        pic_1_draw.point((x, y), fill=new_color(old_color))
pic_1.save("./pic/123.jpg")
pic_1.show()