import re

# match = re.search(r'[1-9]\d{5}','BIT 100081')
# if match:
#     print(match.group(0))

# match = re.match(r'[1-9]\d{5}','BIT 100081')
# if match:
#     print(match.group(0))
# match = re.match(r'[1-9]\d{5}','100081 BIT ')
# if match:
#     print(match.group(0))

# ls = re.findall(r'[1-9]\d{5}','BIT 100081 TSU100084')
# print(ls)

# split = re.split(r'[1-9]\d{5}','BIT 100081 TSU100084')
# print(split)
# split = re.split(r'[1-9]\d{5}','BIT 100081 TSU100084',maxsplit=1)
# print(split)

# for m in re.finditer(r'[1-9]\d{5}','BIT100081 TSU100084'):
#     if m:
#         print(m.group(0))

# sub = re.sub(r'[1-9]\d{5}',':zipcode','BIT100081 TSU100084')
# print(sub)
#
# match = re.search(r'[1-9]\d{5}','BIT 100081')
# if match:
#     print(match.group(0))

# m = re.search(r'[1-9]\d{5}','BIT100081 TSU100084')
# print(m.string,m.re,m.pos,m.endpos)
# print(m.group(0),m.start(),m.end(),m.span())

# 贪婪匹配
match = re.search(r'PY.*N','PYANBNCNDN')
print(match.group(0))
# 最小匹配
match = re.search(r'PY.*?N','PYANBNCNDN')
print(match.group(0))