import requests

r = requests.get('http://www.baidu.com')
r.encoding = r.apparent_encoding
# print(r.status_code,r.text)
# print(r.headers)

# 爬取网页的通用代码框架
def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url, headers=kv ,timeout=30)
        r.raise_for_status()    # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__=="__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))