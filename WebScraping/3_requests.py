import requests
res = requests.get("http://google.com")
res.raise_for_status()

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드", res.status_code, "]")


print(len(res.text))

with open("myGoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)