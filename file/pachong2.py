import os
import requests
from bs4 import BeautifulSoup

# 创建存储音乐的文件夹
if not os.path.exists('music'):
    os.makedirs('music')

# 提示用户输入歌手名
singer = input('请输入歌手名：')

# 构造搜索URL
url = f'https://music.163.com/search/'
params = {
    's': singer,
    'type': 1,  # 搜索类型为歌手
}

# 发起搜索请求
response = requests.get(url, params=params)

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(response.text, 'html5lib')

# 找到包含歌曲信息的元素
song_elements = soup.find_all('div', class_='srchsongst')

# 遍历歌曲元素并提取信息
for song_element in song_elements:
    song_title = song_element.find('a', class_='tit').text.strip()
    song_url = 'https://music.163.com' + song_element.find('a', class_='tit')['href']

    # 下载歌曲
    song_response = requests.get(song_url)
    with open(f'music/{song_title}.mp3', 'wb') as file:
        file.write(song_response.content)

    print(f'已下载歌曲：{song_title}')

print('所有歌曲下载完成！')
