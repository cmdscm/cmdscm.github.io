#导入模块
from lxml import etree
import requests
#定义数字i
i=10000
#转化i成字符串
str_i=str(i)
#得到i长度
long=len(str_i)
while long <= 6:
        #转化i成字符串
        str_i=str(i)
        #得到i长度
        long=len(str_i)
        #开始检测i长度是否为6
        if long < 6 :
                #如果不是开始循环 (6-i长度) 次
                for j in range( 6 - long) :
                        #给i加上0
                        str_i = "0" + str_i
                        #print(str_i)
        #将i加入，组成新的网址
        url=f'http://kaoshi.ac.cn/axis/cpp/p/{str_i}.html'
        #得到网址代码，并设置
        ydm = requests.get(url)
        ydm.encoding='utf-8'
                #print(ydm.text)
        #解析
        et = etree.HTML(ydm.text)
        video_links =et.xpath("//body/video/@src")
        #检测是否有视频
        if not video_links:
                print(str_i)
        else:
                print('有视频')
                #print(video_links)
                #print(i)
        #将i设置为数字
        i=int(str_i)
        i=i+1
        #再次循环
print("完成")

