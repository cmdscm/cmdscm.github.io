import requests

url="https://fanyi.baidu.com/sug"

sj={
    "kw": input("请输入你想翻译的词")
}
ydm =requests.post(url,data=sj)

#print(ydm.text)
print(ydm.json())
