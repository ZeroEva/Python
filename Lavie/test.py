import time
import cv2

url = "rtsp://admin:LaVie27551808@60.251.145.1:554/chID=1&streamtype=main"
width = 640
height = 360
cam = cv2.VideoCapture(url)
cv2.namedWindow(url)
cv2.moveWindow(url, 0, 0)
while True:
    # I = cv2.resize(I, (width, height), 3)
    start, I = cam.read()
    cv2.imshow(url, I)
    if cv2.waitKey(1000) == 27:
        cv2.destroyAllWindows()
        break
