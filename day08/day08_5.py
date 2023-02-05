# opencv 모듈 추가
# mediapipe 모듈 추가

# 이미지 좌측 상단에 이름 표시 puttext
# 동영상 좌측 상단에 크기 조정 resize

import cv2
import mediapipe as mp

# def ShowImage(img_path):
#     img =cv2.imread(img_path)
#     cv2.putText(img, 'korea', (0, 50), cv2.FONT_ITALIC, 1, (0, 0, 255),2)
#     #          이미지  텍스트     위치        폰트       크기    색깔    두께  
#     cv2.imshow('title', img)
#     cv2.waitKey(0)

# ShowImage('peaple.jpg')

cap = cv2.VideoCapture('person2.mp4')
mp_fd = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils
fd = mp_fd.FaceDetection()

while True:
    success, img = cap.read()
    img = cv2.resize(img, (960, 640))
    if success:
        cv2.imshow('title', img)
    cv2.waitKey(25) & 0xFF == 27


