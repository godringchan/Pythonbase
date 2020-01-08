import cv2 as cv

# 打开图片,变量接收
img = cv.imread(r"./pic/75516679_1427173930789067_1140612652205896611_n.jpg")
# 显示图片
cv.imshow("read_img", img)
# 等待键盘输入,否则不会停留显示,而是一闪而过.单位是毫秒,0为无限等待,知道键盘输入
cv.waitKey(0)

# 释放内存, 由于底层是c++写的,所以调用玩要调用destroyallWindows()
cv.destroyAllWindows()