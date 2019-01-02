
from selenium import webdriver

#使用火狐浏览器
browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("周笔畅")
browser.find_element_by_id("su").click()


