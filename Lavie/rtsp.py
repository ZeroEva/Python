import threading
import mysql.connector
import cv2
import time
from mysql.connector import (connection)

from Lavie.IPCamCapture import IPCamCapture

cnx = connection.MySQLConnection(user='root',
                                 password='Pa55w0rd!s',
                                 host='10.10.111.103',
                                 database='lavie')
cursor = cnx.cursor()
query = "SELECT identification FROM t_device WHERE device_type_id = '08'"
cursor.execute(query)
result = cursor.fetchall()

urls = []
for href in result:
    urls.append(href[0])
    print(href[0])


# for i in range(0, 47):
#     urls.append("rtsp://admin:LaVie27551808@60.251.145.1:554/chID=" + str(i + 1) + "&streamtype=main")

xStart = 100
yStart = 100


def worker(url, x_start, y_start):
    width = 640
    height = 360
    cam = IPCamCapture(url)
    cam.start()
    cv2.namedWindow(url)
    cv2.moveWindow(url, x_start, y_start)
    while True:
        I = cam.get_frame()
        cv2.imshow(url, cv2.resize(I, (width, height), 3))
        if cv2.waitKey(1000) == 27:
            cv2.destroyAllWindows()
            cam.stop()
            break


for myUrl in urls:
    threading.Thread(target=worker, args=[myUrl, xStart, yStart]).start()
    xStart += 50
    yStart += 50
