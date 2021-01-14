from bs4 import BeautifulSoup
import requests

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text

# soup = BeautifulSoup("<html>data</html>","html.parser")
# soup2 = BeautifulSoup(open("D://demo.html"),"html.parser")
soup = BeautifulSoup(demo,"html.parser")

# 标签属性
# print(soup.title)
# print(soup.a)
# print(soup.a.name)
# print(soup.a.parent.name)
# print(soup.a.parent.parent.name)
# tag = soup.a
# print(tag.attrs)
# print(tag.attrs['class'])
# print(tag.attrs['href'])
# print(type(tag.attrs))
# print(type(tag))
# print(soup.a.string)
# print(soup.p.string)
# print(type(soup.p.string))

# 标签文本
# newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>","html.parser")
# print(newsoup.b.string)
# print(type(newsoup.b.string))
# print(newsoup.p.string)
# print(type(newsoup.p.string))

# 下行遍历
# soup = BeautifulSoup(demo,"html.parser")
# print(soup.head)
# print(soup.head.contents)
# print(soup.body.contents)
# for child in soup.body.children:
#     print(child)
# print(len(soup.body.contents))

# 上行遍历
# for parent in soup.a.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)

# 美化标签
print(soup.prettify())
print(soup.a.prettify())



















