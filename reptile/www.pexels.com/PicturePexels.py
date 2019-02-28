import re
import time
import requests
import shutil
import os
import threading
import uuid

from bs4 import BeautifulSoup
from urllib import request

from selenium import webdriver

# 保存图片
pictureTotal = 0
pictureStart = 0
pictureFinish = 0

threadSizeMax = 35
threadSizeNow = 0

search = "galaxy"
path = "popular_photos"

base_url = "https://www.pexels.com/"
search_url = "https://www.pexels.com/search/"
popular_photos = "https://www.pexels.com/popular-photos/"

# url = popular_photos

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/71.0.3578.98 Safari/537.36"
}

if search:
    url = search_url + search
else:
    url = popular_photos
if not os.path.exists(path):
    os.makedirs(path)
# 获取 html 文档
# preUrl = request.Request(url, headers=headers)
# resp = request.urlopen(preUrl)
# html = resp.read().decode('utf-8')
options = webdriver.ChromeOptions()
options.__setattr__("headless", True)
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.get(url)
adjustTimes = 0
while True:
    scrollHeightBefore = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(0.5)
    scrollHeightAfter = driver.execute_script("return document.body.scrollHeight")
    adjustTimes += 1
    if adjustTimes % 10 == 0:
        print("第", adjustTimes, "次调整浏览器滚动条")
        if adjustTimes == 1000:
            break
    if scrollHeightAfter == scrollHeightBefore:
        break
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
driver.close()

# 处理 html 文档
soup = BeautifulSoup(html, features="html.parser")
all_a = soup.find_all('a')
pictures = []
for link in all_a:
    href = link.get('href')
    if not href:
        continue
    pattern = "jpeg"
    if pattern in href:
        pictures.append(href)


def picture_download(pd_url):
    # print(pd_url)
    global threadSizeNow
    global pictureFinish
    filename = path + "/" + uuid.uuid4().hex + ".jpeg"
    r = requests.get(pd_url, stream=True, headers=headers)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    pictureFinish += 1
    threadSizeNow -= 1
    print("第", pictureFinish, "张图片下载完成")


pictureTotal = pictures.__len__()
print("共有", pictureTotal, "张图片")


def wait():
    while True:
        global threadSizeMax
        global threadSizeNow
        if threadSizeNow < threadSizeMax:
            break
        time.sleep(0.5)


f = open('picture.md', 'a')
pictures = re.findall('http.*?/photos/.*?.jpeg', html)
s = set(pictures)
for href in s:
    f.write(f'{href}  \n')
f.close()
# for href in pictures:
#     threading.Thread(target=picture_download, args=[href]).start()
#     threadSizeNow += 1
#     pictureStart += 1
#     print("下载第", pictureStart, "张图片")
#     if threadSizeNow >= threadSizeMax:
#         wait()
