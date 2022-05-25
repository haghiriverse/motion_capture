import cv2 
from cvzone.PoseModule import PoseDetector

video_src = cv2.VideoCapture("video.mp4")

detector = PoseDetector()
while video_src.isOpened():
    _, frame = video_src.read()

    try:
        frame = detector.findPose(frame)

        lmList, bbox_info = detector.findPosition(frame)

        if bbox_info:
            lmStr = ""
            for lm in lmList:
                lmStr += f'{lm[0]}, {lm[1]}, {lm[2]}, '
            print(lmStr)

        cv2.imshow("Video", frame)
    except Exception as e:
        print(e)
        break

    cv2.waitKey(1)