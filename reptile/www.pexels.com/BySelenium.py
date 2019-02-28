import time

from selenium import webdriver

search = "Lamborghini"

base_url = "https://www.pexels.com/"
search_url = "https://www.pexels.com/search/"

options = webdriver.ChromeOptions()
options.__setattr__("headless", False)
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.get(base_url)
while True:
    scrollHeightBefore = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(0.5)
    scrollHeightAfter = driver.execute_script("return document.body.scrollHeight")
    if scrollHeightAfter == scrollHeightBefore:
        break
my_sources = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
driver.close()
