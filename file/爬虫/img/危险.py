#https://desk.zol.com.cn/dongman/
from lxml import etree
import requests
import re
import json
#得到源代码
yuming = "https://desk.zol.com.cn"
url="https://desk.zol.com.cn/pc/"
ydm = requests.get(url)
et = etree.HTML(ydm.text)
ydm.encoding = "gbk"
#筛选
fl = et.xpath("//dl[@class='filter-item first clearfix']/dd[@class='brand-sel-box clearfix']/a/@href")
#for thing in fl:
   # url="https://desk.zol.com.cn" + thing
    #ydm = requests.get(url)
  #  ydm.encoding = "gbk"
   # et = etree.HTML(ydm.text)
   # a=et.xpath("//ul[@class='pic-list2  clearfix']/li/a/@href")
    #for item in a:
     #   lj = yuming + item
        #if ".exe" not in lj:
         #   new_url = lj
          #  img_ydm = requests.get(url)
           # img_ydm.encoding = "gbk"
            #obj = re.compile(r"var deskPicArr.*?=(?P<deskpicarr>.*?);",re.S)
#            resp =obj.search(img_ydm.text)
 #           deskpicstr = resp.group("deskpicarr")
  #          deskpic = json.loads(deskpicstr)
   #         for every in deskpic['list']:
    #            oriSize = every.get("oriSize")
     #           imgsrc = every.get("imgsrc")
      #          new_imgsrc = new_imgsrc.replace("##SIZE##",oriSize)
       #         print(new_imgsrc)
        #        img_name = new_imgsrc.split("/")[-1]
         #       #1.发请求
          #      two_ydm_img = requests.get(new_imgsrc)
           #     with open(f"{img_name}.jpg",mode="wb") as f:
            #
         #       f.write(two_ydm_img.content)
input("爬取完毕")
#print(a)
#'/bizhi/10051_120299_2.html'
#编码经典两种,1是utf-8,2是以gb开头的,直接写
#gbk
#print(ydm.text)
#步骤：先找源码，再找meta看编码方式，然后设置

