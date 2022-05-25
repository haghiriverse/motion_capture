import cv2 
from cvzone.PoseModule import PoseDetector

video_src = cv2.VideoCapture("video.mp4")

detector = PoseDetector()
while video_src.isOpened():
    _, frame = video_src.read()

    try:
        frame = detector.findPose(frame)

        cv2.imshow("Video", frame)
    except Exception as e:
        print(e)
        break

    cv2.waitKey(1)