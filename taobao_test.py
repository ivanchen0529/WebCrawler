import requests
import re

goods = '小型犬'
depth = 2
url = 'https://list.epet.com/search/main.html?keyword=' + goods
infoList = []

kv = {'user-agent': 'Mozilla/5.0'}
r = requests.get(url,headers=kv, timeout = 30)
r.raise_for_status()
r.encoding = r.apparent_encoding
print(r.text)

plt = re.findall(r'data-price\=\"[\d\.]*\"',r.text)
tlt = re.findall(r'data-subject\=\".*?\"', r.text)
#
print(plt)
print(tlt)