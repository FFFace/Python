import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=748105&weekday=thu"
res = requests.get(url)

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs={"class":"title"})

for cartoon in cartoons:
    print(cartoon.a.get_text(), "https://comic.naver.com" + cartoon.a["href"])
