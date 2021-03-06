import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url, code='utf-8'):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""

def getStockList(lst, stockURL):
    html = getHTMLText(stockURL, 'GB2312')
    # 找到所有股票代码信息
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}",href)[0])
        except:
            continue

def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = { }
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})

            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count += 1
                print('\r当前速度：{:.2f}%'.format(count*100/len(lst)),end='')
        except:
            count += 1
            print('\r当前速度：{:.2f}%'.format(count * 100 / len(lst)), end='')
            continue
    return ""

def main():
        stock_list_url = 'http://quote.eastmoney.com/center/gridlist.html#hs_a_board'
        stock_info_url = '' # 股票信息放在静态网页的股票网站
        output_file = 'D://BaiduStockInfo.txt'
        slist = []
        getStockList(slist, stock_list_url)
        getStockInfo(slist, stock_info_url, output_file)

main()
