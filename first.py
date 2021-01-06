import requests

r = requests.get('http://www.baidu.com')
r.encoding = r.apparent_encoding
print(r.status_code,r.text)
print(r.headers)