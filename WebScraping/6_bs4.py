import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.a)                                   # soup 객체의 첫 a element 반환
# print(soup.a.attrs)                             # soup 객체의 a element의 속성 정보 반환
# print(soup.a["href"])                           # soup 객체의 a element 중 href 속성 값 반환

#soup.find("a", attrs={"class" : "Nbtn_upload"})    # soup 객체에서 a element인 class = "Nbtn_upload" 를 반환
#soup.find(attrs={"class" : "Nbtn_upload"})         # soup 객체에서 처음 나오는 class = "Nbtn_upload" 를 반환
#print(soup.find("a", attrs={"class" : "Nbtn_upload"}))

# print(soup.find("li", {"class" : "rank01"}))
rank1 = soup.find("li", {"class" : "rank01"})       # next_sibling : 다음 값 반환
# print(rank1.a.get_text())                           # previous_sibling : 이전 값 반환
# rank2 = rank1.next_sibling.next_sibling
# print(rank2.a.get_text())
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2_2 = rank3.previous_sibling.previous_sibling
# print(rank2_2.a.get_text())

# print(rank1.parent)                                   # parent : 부모 갑 반환
rank2 = rank1.find_next_sibling("li")                   # find_next_sibling(str) : 다음 값 중 str과 동일한 값 반환 
rank1_2 = rank2.find_previous_sibling("li")             # find_previous_sibling(str) : 이전 값 중 str과 동일한 값 반환
lis = rank1.find_next_siblings("li")                    # find_next_siblings(str) : 다음 값 중 str과 동일한 모든 값 반환

webtoon = soup.find("a", text="초인의 시대-후기")
print(webtoon)