from PIL import Image
import matplotlib.pyplot as plt
pic = Image.open(
    r"/media/godring_chan/新加卷/个人资料文件/66315718_151221742663279_2299735626410194223_n.jpg"
)

# pic.show()
plt.imshow(pic)
plt.xticks([])
plt.yticks([])
plt.show()
# print("图片的大小", pic.size)
# print("图片的高度", pic.height)
# print("图片的宽度", pic.width)
# print("图片某点颜色", pic.getpixel((100, 100)))