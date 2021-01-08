import requests
import os

url = "https://vd3.bdstatic.com/mda-kjrx2uu9iyjn6ijk/sc/cae_h264_clips/1603725044/mda-kjrx2uu9iyjn6ijk.mp4"
root = "D://video//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")