from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Edge("./msedgedriver.exe")

#창 최대화
browser.maximize_window()

#링크 이동
url = "https://flight.naver.com/flights/"
browser.get(url)

#가는날 선택
browser.find_element_by_link_text("가는날 선택").click()

# #이번달 28, 30 선택
# browser.find_elements_by_link_text("28")[0].click()
# browser.find_elements_by_link_text("30")[0].click()

# #다음달 28, 30 선택
# browser.find_elements_by_link_text("28")[1].click()
# browser.find_elements_by_link_text("30")[1].click()

#이번달 28, 다음달 30 선택
browser.find_elements_by_link_text("28")[0].click()
browser.find_elements_by_link_text("30")[1].click()

#제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]/div/span").click()

#항공권 선택
browser.find_element_by_link_text("항공권 검색").click()

#browser 대기. 최대 10초, BY.XPATH("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")가 나올때 까지
try:
    elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text)
finally:
    browser.quit()