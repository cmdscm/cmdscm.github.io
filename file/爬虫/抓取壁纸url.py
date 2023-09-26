#https://desk.zol.com.cn/dongman/
from lxml import etree
import requests
yuming = "https://desk.zol.com.cn"
url="https://desk.zol.com.cn/pc/"
ydm = requests.get(url)
et = etree.HTML(ydm.text)
ydm.encoding = "gbk"
fl = et.xpath("//dd[@class='brand-sel-box clearfix']/a/@href")
for thing in fl:
    url="https://desk.zol.com.cn" + thing
    ydm = requests.get(url)
    ydm.encoding = "gbk"
    et = etree.HTML(ydm.text)
    a=et.xpath("//ul[@class='pic-list2  clearfix']/li/a/@href")
    for item in a:
        lj = yuming + item
        print(lj)
input("爬取完毕")
#print(a)
#'/bizhi/10051_120299_2.html'
#编码经典两种,1是utf-8,2是以gb开头的,直接写
#gbk
#print(ydm.text)
#步骤：先找源码，再找meta看编码方式，然后设置

