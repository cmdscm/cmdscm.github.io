from lxml import etree
import requests
import re
import json

base_url = "https://desk.zol.com.cn"

def get_wallpapers():
    url = "https://desk.zol.com.cn/fengjing/"
    response = requests.get(url)
    response.encoding = "gbk"
    et = etree.HTML(response.text)

    img_links = et.xpath("//ul[@class='pic-list2  clearfix']/li/a/@href")
    for link in img_links:
        full_link = base_url + link
        if ".exe" not in full_link:
            response = requests.get(full_link)
            response.encoding = "gbk"
            obj = re.compile(r"var deskPicArr.*?=(?P<deskpicarr>.*?);", re.S)
            resp = obj.search(response.text)
            if resp is not None:
                deskpicstr = resp.group("deskpicarr")
                deskpic = json.loads(deskpicstr)
                for item in deskpic['list']:
                    oriSize = item.get("oriSize")
                    imgsrc = item.get("imgsrc")
                    new_imgsrc = imgsrc.replace("##SIZE##", oriSize)
                    print(new_imgsrc)
                    img_name = new_imgsrc.split("/")[-1]
                    # 发起请求下载图片
                    img_response = requests.get(new_imgsrc)
                    if img_response.status_code == 200:
                        with open(f"{img_name}.jpg", mode="wb") as f:
                            f.write(img_response.content)
                        print(f"已成功下载图片：{img_name}")
                    else:
                        print(f"下载图片失败：{img_name}")
            else:
                print("未能匹配到图片信息")

    input("爬取完毕")


if __name__ == "__main__":
    get_wallpapers()
