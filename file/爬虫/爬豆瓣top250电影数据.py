import requests
import re
for i in range(1, 11):
    yeshu = (i - 1) * 25
    url = f"https://movie.douban.com/top250?start={yeshu}&filter="
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36"
    }
    sj = requests.get(url, headers=head)
    sj.encoding = "utf-8"

    obj = re.compile(
        r'<div class="item">.*?<em class="">(?P<xvhao>.*?)</em>.*?<span class="title">(?P<name>.*?)</span>'
        r'.*?<br>(?P<year>.*?)&nbsp'
        r'.*?<span class="rating_num" property="v:average">'
        r'(?P<pf>.*?)</span>.*?<span>(?P<pjrs>.*?)'
        r'</span>.*?<span class="inq">(?P<say>.*?)</span>', re.S)

    tqsj = obj.finditer(sj.text)

    with open("豆瓣前top250部电影数据.txt", "a", encoding="utf-8") as file:
        for item in tqsj:
            dic = item.groupdict()
            dic['year'] = dic['year'].strip()
            file.write(str(dic) + "\n")
