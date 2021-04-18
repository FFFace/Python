import requests
import re
from bs4 import BeautifulSoup

soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img",attrs={"class":"thumb_img"})

for year in range(2015, 2020):

    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()

    for index, image in enumerate(images):
        item = image["src"]
        if item.startswith("//"):
            item = "https:" + item
            
        image_res = requests.get("item")
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, index+1),"wb") as f:
            f.write(image_res.content)

        if index > 5:
            break
