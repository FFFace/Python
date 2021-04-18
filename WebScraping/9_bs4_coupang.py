import requests
import re
from bs4 import BeautifulSoup

for i in range(1,6):
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for item in items:
        ad = item.find("span", attrs={"class":"ad-badge-text"})
        if ad:
            print("<광고 제품>")
            continue
        title = item.find("div", attrs={"class":"name"}).get_text()
        price = item.find("strong",attrs={"class":"price-value"}).get_text()
        rating = item.find("em",attrs={"class":"rating"})
        if rating:
            rate = rating.get_text()
            if float(rate) < 4.5:
               print("<평점 미달>")
               continue 

        else:
            print("<평점 미달>")
            continue

        ratingTotal = item.find("span", attrs={"class":"rating-total-count"})
        if ratingTotal:
            ratingCount = ratingTotal.get_text()
            ratingCount = ratingCount[1:-1]
            if int(ratingCount) < 4.5:
                print("<평점 미달>")
                continue
        else:
            print("<평점 없음>")
            continue
        
        rink = item.find("a",attrs={"class":"search-product-link"})["href"]


        print(f"상품 명 : {title}")
        print(f"가격 : {price}")
        print(f"평점 :{rate} ({ratingCount})")
        print(f"링크 : https://www.coupang.com{rink}")
        print("-"*20)