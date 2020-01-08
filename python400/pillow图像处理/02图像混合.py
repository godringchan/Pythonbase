import PIL.Image as Img

pic1 = Img.open(r"./pic/74940708_597084071101468_1743623235751749021_n.jpg"
                ).convert(mode="RGB")
# pic2 = Img.open(r"./pic/75516679_1427173930789067_1140612652205896611_n.jpg"
#                 ).convert(mode="RGB")
pic3 = Img.open(r"./pic/79385082_757362084730951_437985903676532002_n.jpg"
                ).convert(mode="RGB")
# pic4 = Img.new("RGB", pic1.size, "red")  # new相当于创建一个图层
Img.blend(pic1, pic3, alpha=0.5).show()  # 透明图混合图片

# print(pic.size, pic2.size, pic3.size)
