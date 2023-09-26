import requests
import json
import re
#访问详情页，提取js里面的var xxxxxxx
# 分析imgsrc,xx
# 下载
url ="https://desk.zol.com.cn/bizhi/10051_120299_2.html"
ydm = requests.get(url)
ydm.encoding = "gbk"
#print(ydm.text)
obj = re.compile(r"var deskPicArr.*?=(?P<deskpicarr>.*?);",re.S)
resp =obj.search(ydm.text)
deskpicstr = resp.group("deskpicarr")
#print(deskpicstr)
deskpic = json.loads(deskpicstr)
#print(deskpic)
for item in deskpic['list']:
    oriSize = item.get("oriSize")
    imgsrc = item.get("imgsrc")
    imgsrc = imgsrc.replace("##SIZE##",oriSize)
    print(imgsrc)
    imgname = imgsrc.split("/")[-1]
    #1.发请求
    ydm_img = requests.get(imgsrc)
    with open(f"{imgname}.jpg",mode="wb") as f:
        f.write(ydm_img.content)
    #break




