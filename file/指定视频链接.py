import requests
from lxml import etree

url = input('请输入视频链接:')
if url == '':
    url = 'https://www.bilibili.com/video/BV1qk4y1Q7LB/?spm_id_from=333.999.0.0&vd_source=c052e17dad74a9e545ae369e2d3b6d20'
# print(url)

headers = {
    'Authority':'api.bilibili.com',
    'Method':'GET',
    'Path':'/x/kv-frontend/namespace/data?appKey=333.1333&versionId=1701398565806&nscode=0',
    'Scheme':'https','Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Origin':'https://m.bilibili.com',
    'Referer':'https://m.bilibili.com/video/BV1qk4y1Q7LB/?spm_id_from=333.999.0.0&vd_source=c052e17dad74a9e545ae369e2d3b6d20',
    'Sec-Ch-Ua':'"Not.A/Brand";v="8", "Chromium";v="114"',
    'Sec-Ch-Ua-Mobile':'?1',
    'Sec-Ch-Ua-Platform':'"Android"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-site',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Mobile Safari/537.36'
}

def findlink(video:str):# 返回视频网址
    return video.split('"readyVideoUrl":"')[1].split('","readyDuration"')[0]

sj = requests.get(url, headers=headers)
sj.encoding = 'utf-8'
sj = sj.text
et = etree.HTML(sj)

title = et.xpath("//title/text()")[0][:-14]
if title == '':
    title = 'Title'
video = et.xpath("//body/div[@id='app']/div[@class='video']/div[@data-v-55ca5b53]/div[@data-v-55ca5b53]/div[@class='m-video-player']/div[@class='player-container']/div[@data-v-07bebd93]/script[@type='text/javascript']/text()")

url = findlink(video[0])
sj = requests.get(url, stream=True, headers=headers)# 下载视频
with open(f'E:\\vscode5月27日下载\\文件\\保存爬取文件处\\{title}.mp4','wb') as mp4:
    for chunk in sj.iter_content(chunk_size=1024*1024):
        if chunk:
            mp4.write(chunk)

'''
https://cn-hbwh-cm-01-01.bilivideo.com/upgcxcode/08/44/1405144408/1405144408-1-16.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1720012034&gen=playurlv2&os=bcache&oi=1973600893&trid=00006ffe9af24a394fe1a0bc2b12e2acb12ah&mid=0&platform=html5&og=hw&upsig=b22ecd137038269aaf6aae9d8acc1e6e&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=10197&bvc=vod&nettype=0&f=h_0_0&bw=33418&logo=80000000
'''
