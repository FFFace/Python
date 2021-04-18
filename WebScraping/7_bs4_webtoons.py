import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("a", attrs={"class" : "title"})
#네이버 웹툰 모든 요일별 웹툰 가져오기
#class가 title인 모든 a element 반환
for cartoon in cartoons:
    print(cartoon.get_text())