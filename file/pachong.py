
import requests
import urllib
import json
import time
from urllib import parse

#1.抓取所有的分类的id，然后拼接出对应的分类的链接
#2.访问分类的链接，抓取所有歌单(专辑)的详细页面的链接
#3.访问详细页面的链接，抓取所有歌曲的详细页面的链接
#4.抓取歌曲的信息(歌名,歌手名,分类信息)，存储到文本(csv或者txt等)或数据库里
#5,将歌曲名传递给download_music实现，下载对应音乐文件(这个操作可以只下载一首)


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    'referer': 'https://y.qq.com/portal/playlist.html',
}

start_url = 'https://c.y.qq.com/splcloud/fcgi-bin/fcg_get_diss_by_tag.fcg?' \
      'picmid=1&rnd=0.34692207151847465&g_tk=5381&' \
      'jsonpCallback=getPlaylist&loginUin=0&hostUin=0&format=jsonp&' \
      'inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&' \
      'needNewCode=0&categoryId=10000000&sortId=5&sin={0}&ein={1}'

sin = 0
ein = 29
num = 1
while True:
    response = requests.get(start_url.format(sin,ein),headers = headers).text
    dissid_dic = json.loads(response.strip('getPlaylist()'))
    for item in dissid_dic['data']['list']:
        disstid = item['dissid']  #获取歌单 id
        dissname = item['dissname']  #获取歌单名称
        time.sleep(1)

        '''
            二、通过dissid 获取 songmid
        '''
        songmid_url = 'https://c.y.qq.com/qzone/fcg-bin/fcg_ucc_getcdinfo_byids_cp.fcg?' \
                      'type=1&json=1&utf8=1&onlysong=0&disstid={0}&' \
                      'format=jsonp&g_tk=5381&jsonpCallback=playlistinfoCallback&' \
                      'loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&' \
                      'outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
        headers['referer'] = 'https://y.qq.com/n/yqq/playsquare/3806226626.html'
        response = requests.get(songmid_url.format(disstid),headers = headers).text
        song_dic = json.loads(response.strip('playlistinfoCallback()'))
        # print(song_dic)
        songnum = 1
        for songmids in song_dic['cdlist'][0]['songlist']:
            songmid = songmids['songmid']  #获取songmid
            if (('*' or '**') or '/') in songmids['songname']:
                songname = 'ssss'
            else:
                songname = songmids['songname'] #获取songname

            #组装filename
            filename = 'C400{}.m4a'.format(songmid)

            # print(songmid)
            # print(filename)
            time.sleep(1)

            '''
                三、获取vkey
            '''
            vkey_url = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?' \
                       'g_tk=5381&jsonpCallback=MusicJsonCallback&' \
                       'loginUin=0&hostUin=0&format=json&inCharset=utf8&' \
                       'outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&' \
                       'cid=205361747&callback=MusicJsonCallback&' \
                       'uin=0&songmid={0}&filename={1}&' \
                       'guid=1093240106'
            headers['referer'] = 'https://y.qq.com/portal/player.html'
            response = requests.get(vkey_url.format(songmid,filename),headers = headers).text
            vek_dic = json.loads(response.strip('MusicJsonCallback()'))
            #提取vkey
            vkey = vek_dic['data']['items'][0]['vkey']
            # print(vkey)
            '''
                四、通过vkey 下载音乐
            '''
            music_url = 'http://dl.stream.qqmusic.qq.com/C400{0}.m4a?vkey={1}&guid=1093240106&uin=0&fromtag=66'

            headers['Host'] = 'dl.stream.qqmusic.qq.com'
            del headers['referer']

            response = requests.get(music_url.format(songmid,vkey),headers = headers,stream = True).raw.read()

            #写入文件
            with open('music/{0}.mp3'.format(songname),'wb') as file:
                file.write(response)
            time.sleep(1)

            print('第{0}页，{1}歌单{2}首歌曲：{3}'.format(num,dissname,songnum,songname))
            songnum+=1
    #下一页
    sin+=30
    ein+=30
    num+=1
    time.sleep(2)
    if sin > 6075:
        break