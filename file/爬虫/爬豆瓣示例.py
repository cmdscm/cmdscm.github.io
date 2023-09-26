'''
豆瓣top250

名称、发布年限，评分，评分人数

1.源代码
2.re正则提取
3.存储文件
'''

import requests
import re
url = "https://movie.douban.com/top250"



head={
    #UA,服务器对设备进行检测
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36"
}
sj = requests.get(url,headers=head)#处理反爬
sj.encoding="utf-8"
#print(sj.text)

obj=re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
               r'.*?<br>(?P<year>.*?)&nbsp'
               r'.*?<span class="rating_num" property="v:average">'
               r'(?P<pf>.*?)</span>.*?<span>(?P<pjrs>.*?)'
               r'</span>',re.S)#re.S可以让re匹配换行符

tqsj=obj.finditer(sj.text)
for item in tqsj:
    dic = item.groupdict()
    dic['year'] = dic['year'].strip()#去掉年份左右的空白（空格，制表符）
    print(dic)