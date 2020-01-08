import cv2 as cv


def face_detect_demo(pic):
    # 转灰度图片
    gray_pic = cv.cvtColor(pic, cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier(
        r"/home/godring_chan/opencv/opencv-4.1.2/data/haarcascades/haarcascade_frontalface_default.xml"
    )
    faces = face_detect.detectMultiScale(gray_pic)
    for x, y, w, h in faces:
        cv.rectangle(pic, (x, y), (x + w, y + h),
                     color=(0, 255, 0),
                     thickness=2)
    cv.imshow("", pic)


pic = cv.imread(r"./pic/75516679_1427173930789067_1140612652205896611_n.jpg")
# cv.imshow("", pic)
face_detect_demo(pic)
cv.waitKey(0)
cv.destroyAllWindows()