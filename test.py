import requests
from bs4 import BeautifulSoup
import re

url = "http://www.shanghairanking.cn/rankings/bcur/2020"
r = requests.get(url, timeout = 30)
r.raise_for_status()
r.encoding = r.apparent_encoding
html = r.text

soup = BeautifulSoup(html, "html.parser")
for tr in soup.find('tbody'):
    tds = tr('td')
    print(tds[0].text)