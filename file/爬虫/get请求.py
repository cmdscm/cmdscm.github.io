import requests

#baidu

url = "http://www.baidu.com"

ydm =requests.get(url)
ydm.encoding = 'utf-8'
#print(ydm.text) #拿到页面源代码

#写入文件

with open("mybaidu.html" ,mode="w",encoding='utf-8') as f:
    f.write(ydm.text)
