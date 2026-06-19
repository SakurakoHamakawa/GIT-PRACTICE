import requests, json
from bs4 import BeautifulSoup

url = "http://abehiroshi.la.coocan.jp/movie/eiga.htm"

res = requests.get(url)
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text, "html.parser")

performance_list = []

movie_list = soup.find_all('table')[1].find_all('tr')

for movie in movie_list:
    performance_list.append(movie.find_all('td')[1].text)

print(json.dumps(performance_list, ensure_ascii=False, indent=2))