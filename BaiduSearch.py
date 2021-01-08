import requests

keyword = 'Python'
hd = {'user-agent':'Mozilla/5.0'}
try:
    kv = {'wd':keyword}
    r = requests.get("http://www.baidu.com/s", headers=hd ,params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
    print(r.headers)
except:
    print("爬取失败")