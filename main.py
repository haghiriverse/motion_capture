import cv2 
from cvzone.PoseModule import PoseDetector

video_src = cv2.VideoCapture("video.mp4")

while video_src.isOpened():
    _, frame = video_src.read()

    cv2.imshow("Video", frame)
    cv2.waitKey(1)