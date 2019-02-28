import cv2
import threading


class IPCamCapture:
    def __init__(self, url):
        self.Frame = []
        self.status = False
        self.isStop = False

        # 攝影機連接。
        self.capture = cv2.VideoCapture(url)

    def start(self):
        # 把程式放進子執行緒，daemon=True 表示該執行緒會隨著主執行緒關閉而關閉。
        print('ipcam started!')
        threading.Thread(target=self.query_frame, daemon=True, args=()).start()

    def stop(self):
        # 記得要設計停止無限迴圈的開關。
        self.isStop = True

    def get_frame(self):
        # 當有需要影像時，再回傳最新的影像。
        return self.Frame

    def query_frame(self):
        while not self.isStop:
            self.status, self.Frame = self.capture.read()
        self.capture.release()
