import requests
import re
for i in range(1,11):
    page = (i - 1) * 25
    url=f"https://movie.douban.com/top250?start={page}&filter="
    print(url)