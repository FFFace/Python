import requests
import re
import time
import csv
import os
from bs4 import BeautifulSoup

url1 = "https://finance.naver.com/sise/sise_group.nhn?type=upjong"
res1 = requests.get(url1)
succece = res1.status_code

if succece == 200:
    soup1 = BeautifulSoup(res1.text, "lxml")
    jongAll = soup1.find_all("td", attrs={"style":re.compile("^padding")})
    print("-------전체 종목-------")
    for jong in jongAll:
        print(jong.get_text())
    selecteJong = input("종목을 입력하세요. :")
    day = time.strftime("_%Y_%m_%d", time.localtime(time.time()))
    filepath = "./infos"
    if os.path.exists("./infos") == False:
        os.mkdir("./infos")
    filename = "./infos/" +selecteJong + day + ".csv"

    f = open(filename, "w", encoding="utf-8-sig", newline="")
    writer = csv.writer(f)
    for jong in jongAll:
        if jong.get_text() == selecteJong:
            link = "https://finance.naver.com/" + jong.a["href"]
            res2 = requests.get(link)
            res2.raise_for_status()
            soup2 = BeautifulSoup(res2.text, "lxml")
            title = "종목명	현재가	전일비	등락률	매수호가	매도호가	거래량	거래대금	전일거래량".split("\t")
            writer.writerow(title)
            dataTable = soup2.find("tbody").find_all("tr")

            for datas_row in dataTable:
                datas = datas_row.find_all("td")
                data = [column.get_text().strip() for column in datas]
                if len(data) <= 1:
                    continue
                writer.writerow(data)

            break
        print("Cant Found Stock Item!! Your's Enter :", selecteJong)

else:
    print("Error! requests failed!")
    print("url =", url, "code =", res.status_code)
