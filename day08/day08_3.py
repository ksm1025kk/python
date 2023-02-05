import cv2
import mediapipe as mp
# pip install mediapipe

cap = cv2.VideoCapture('person.mp4')
mp_fd = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils
fd = mp_fd.FaceDetection(0.8)                                  # 정확도 조정

while True:
    success, img = cap.read()
    # 동영상을 성공적으로 읽었으면 보여주기 전에 얼굴을 먼저 찾는다
    if success:
        from_bgr_to_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # 얼굴찾기 정확도 향상을 위해 bgr -> rgb
        face = fd.process(from_bgr_to_rgb)
        # 얼굴 찾기


        if face.detections:
            for id, detection in enumerate(face.detections):
                # mp_draw.draw_detection(img, detection)        mefiapipe 얼굴표시
                fd_box = detection.location_data.relative_bounding_box
                box = int(fd_box.xmin * img.shape[1]), int(fd_box.ymin * img.shape[0]), int(fd_box.width * img.shape[1]), int(fd_box.height * img.shape[0])
                cv2.rectangle(img, box, (255, 0, 255), 2)
                cv2.putText(img, f'{round(detection.score[0]*100, 1)}%', (box[0], box[1]), cv2.FONT_ITALIC, 1, (255, 0, 255), 2)

        cv2.imshow('title', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break