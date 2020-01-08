import cv2 as cv
cv_pic = cv.imread(
    r"./pic/75516679_1427173930789067_1140612652205896611_n.jpg")
cv_resize_pic = cv.resize(cv_pic, dsize=(300, 400))
print("修改后图片的形状", cv_resize_pic.shape)
cv.imshow("resize_img", cv_resize_pic)

# cv.waitKey(0)
# 只有输入q才退出
# code = cv.waitKey(0)
while True:
    if ord("q") == cv.waitKey(0):
        break

cv.destroyAllWindows()
