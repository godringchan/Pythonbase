import cv2 as cv
# 打开图片
pic = cv.imread(r"./pic/75516679_1427173930789067_1140612652205896611_n.jpg")
# 图片转换了灰色
gray_pic = cv.cvtColor(pic, code=cv.COLOR_BGR2GRAY)
# 读取图片
cv.imshow("BGR_img", pic)
cv.imshow("gray_img", gray_pic)
# 保存灰色图片
cv.imwrite("gray_img_name.jpg", gray_pic)
# 等待键盘输入,关闭窗口
cv.waitKey(0)
# 清空内存
cv.destroyAllWindows()
