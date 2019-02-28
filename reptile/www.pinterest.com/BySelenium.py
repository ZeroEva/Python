import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

base_url = "https://www.pinterest.com/"
google_username = "hao.sunshine.eva@gmail.com"
google_password = "hao0822.."

options = webdriver.ChromeOptions()
options.__setattr__("headless", False)
driver = webdriver.Chrome(chrome_options=options)
# driver.maximize_window()
driver.get(base_url)
# driver.add_cookie('''sessionFunnelEventLogged=1; G_ENABLED_IDPS=google; csrftoken=6jwgXot1tXYvd4MXcKgPbUy8k9hEbazp; _b="AT0Fw/qCo0JIqp4MbqybLnLIgkTT2BnZRAYXTsCHDlmoZ9U70x1glX9amTEjBBY+mTY="; bei=false; cm_sub=none''')
button = driver.find_element_by_class_name("GoogleConnectButton")
button.click()
current = driver.current_window_handle
''' 输入用户名 '''
handles = driver.window_handles
handles.remove(current)
driver.switch_to.window(handles[0])
name = driver.find_element_by_name("identifier")
name.send_keys(google_username)
name.send_keys(Keys.ENTER)
''' 输入密码 '''
time.sleep(1)
name = driver.find_element_by_name("password")
name.send_keys(google_password)
name.send_keys(Keys.ENTER)
''' 切换回当前窗口 '''
driver.switch_to.window(current)
# while True:
#     scrollHeightBefore = driver.execute_script("return document.body.scrollHeight")
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#     time.sleep(0.5)
#     scrollHeightAfter = driver.execute_script("return document.body.scrollHeight")
#     if scrollHeightAfter == scrollHeightBefore:
#         break
# html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
# print(html)
# print("===========================================================================")
# driver.close()
time.sleep(10)
print("=======")
driver.find_element_by_css_selector("")
body = driver.execute_script("return document.getElementsByClassName('Masonry')[0].innerHTML")
print(body)
driver.close()
