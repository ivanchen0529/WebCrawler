import requests
import re

def getHTMLText(url):
    print("")

def parsePage(ilt, html):
    print("")

def printGoodsList(ilt):
    print("")

def main():
    goods = 'Nike'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue

