import cv2 
from cvzone.PoseModule import PoseDetector
import os

video_src = cv2.VideoCapture(os.getenv("VIDEO_FILE"))

detector = PoseDetector()
posList  = []

while video_src.isOpened():
    _, frame = video_src.read()

    try:
        frame = detector.findPose(frame)

        lmList, bbox_info = detector.findPosition(frame)

        if bbox_info:
            lmStr = ""
            for lm in lmList:
                lmStr += f'{lm[1]}, {frame.shape[0] - lm[2]}, {lm[3]},'
            posList.append(lmStr)

        cv2.imshow("Video", frame)
    except Exception as e:
        print(e)
        break

    cv2.waitKey(1)

with open("AnimationList.txt", "w") as f:
    for pos in posList:
        f.write(f'{pos}\n')