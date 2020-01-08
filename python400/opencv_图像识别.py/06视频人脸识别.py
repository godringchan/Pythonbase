import cv2 as cv


def face_detect_demo(flame):
    # 图像变灰提高识别速度
    gray = cv.cvtColor(flame, cv.COLOR_BGR2GRAY)
    # 加载脸部识别数据
    face_detect = cv.CascadeClassifier(
        r"/home/godring_chan/opencv/opencv-4.1.2/data/haarcascades/haarcascade_frontalface_default.xml"
    )
    # 使用识别数据识别图像
    faces = face_detect.detectMultiScale(gray)
    # 获取脸部的坐标，绘制矩形
    for x, y, w, h in faces:
        cv.rectangle(flame, (x, y), ((x + w), (y + h)),
                     thickness=3,
                     color=(0, 0, 255))
        cv.circle(flame,
                  center=(x + (w // 2), y + (h // 2)),
                  radius=(w // 2),
                  thickness=2,
                  color=(0, 255, 0))
    # 播放绘制好的图像
    cv.imshow("", flame)


video = cv.VideoCapture(r"./pic/000dwH8Mlx07yW3q31T201041201OsP80E010.mp4")

# 循环检测视频中的图像
while True:
    flag, flame = video.read()
    if not flag:
        break
    face_detect_demo(flame)
    if ord("q") == cv.waitKey(1):
        break

cv.destroyAllWindows()
video.release()