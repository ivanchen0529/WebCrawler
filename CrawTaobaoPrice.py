import requests
import re

def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
def parsePage(ilt, html):
    try:
        plt = re.findall(r'data-price\=\"[\d\.]*\"',html)
        tlt = re.findall(r'data-subject\=\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split('=')[1])
            title = eval(tlt[i].split('=')[1])
            ilt.append([price,title])
    except:
        print("")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = '小型犬'
    depth = 5
    start_url = 'https://list.epet.com/search/main.html?keyword=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&page=' + str(i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()

