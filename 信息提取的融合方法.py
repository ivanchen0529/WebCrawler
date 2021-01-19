from bs4 import BeautifulSoup
import requests
import re

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))

# 查找a标签
print(soup.find_all('a'))
# 查找a标签和b标签
print(soup.find_all(['a','b']))

# True表示所有标签信息
for tag in soup.find_all(True):
    print(tag.name)

# 显示所有b开头的标签名
for tag in soup.find_all(re.compile('b')):
    print(tag.name)

# 查找p标签中带有course字符串的信息
print(soup.find_all('p','course'))

# 直接定义属性
print(soup.find_all(id='link1'))

# 用正则找带link的信息
print(soup.find_all(id=re.compile('link')))

# 不带儿子节点
print(soup.find_all('a',recursive=False))

# 检索字符串信息
print(soup.find_all(string = "Basic Python"))

# 正则检索字符串关于Python的
print(soup.find_all(string = re.compile("python")))


