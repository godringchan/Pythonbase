import cv2 as cv

cv_pic = cv.imread(
    r"./pic/75516679_1427173930789067_1140612652205896611_n.jpg")

# 坐标
x, y, width, height = 350, 450, 80, 80
#  绘制矩形thickness线条的宽度,color线条的颜色
cv.rectangle(cv_pic, (x, y, x + width, y + height),
             thickness=2,
             color=(0, 255, 0))  # cv的颜色是bgr模式
# 绘制圆形center指的是远点坐标,radius半径
cv.circle(cv_pic, center=(x, y), radius=(80), color=(0, 0, 255), thickness=3)
cv.imshow("", cv_pic)
cv.waitKey(0)
cv.destroyAllWindows()
