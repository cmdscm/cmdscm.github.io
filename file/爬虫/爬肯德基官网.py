import requests

url="http://www.kfc.com.cn/kfccda/storelist/index.aspx"
sj={
    'cname':'新余',
    'pid':'',
    'keyword': '抱石',
    'pageIndex': 1,
    'pageSize': 10
} 
ydm=requests.post(url,data=sj)

print(ydm.json())