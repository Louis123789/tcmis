import requests
from bs4 import BeautifulSoup

url = "view-source:https://www.atmovies.com.tw/movie/next/"
Data = requests.get(url)
Data.encoding = "utf-8"
#print(Data.text)
sp = BeautifulSoup(Data.text, "html.parser")
result=sp.find("td iframe")
for item in result:
	print(item.get("src"))
