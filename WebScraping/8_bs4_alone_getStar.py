import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=748105&weekday=thu"
res = requests.get(url)

soup = BeautifulSoup(res.text, "lxml")

cartoonsTitle = soup.find_all("td", attrs={"class":"title"})
cartoonsRating = soup.find_all("div", attrs={"class":"rating_type"})

count = range(0, len(cartoonsTitle))

for num in count:
    print(cartoonsTitle[num].a.get_text(), cartoonsRating[num].strong.get_text())