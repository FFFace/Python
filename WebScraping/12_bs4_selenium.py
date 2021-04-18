import time
from selenium import webdriver

#브라우저 열기
browser = webdriver.Edge("./msedgedriver.exe")

#네이버로 이동
browser.get("http://naver.com")

#로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

time.sleep(3)

#로그인 
browser.find_element_by_id("id").send_keys("naverID")
browser.find_element_by_id("pw").send_keys("passward")
browser.find_element_by_id("log.login").click()

time.sleep(1)

browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("another_Id")

print(browser.page_source)

time.sleep(2)
browser.quit()