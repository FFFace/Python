import requests

url = "http://google.com"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68"}
res = requests.get(url, headers = headers)
res.raise_for_status()



print(len(res.text))

with open("myGoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)