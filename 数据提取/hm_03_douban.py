"""
    豆瓣电影爬虫
"""

import requests
from lxml import etree

# 1. 将目标网站上的页面抓取下来
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/64.0.3282.167 Safari/537.36',
    'Referer': 'https://movie.douban.com/'
}
url = 'https://movie.douban.com/'
resp = requests.get(url, headers=headers)
text = resp.text
# print(text)

# 2. 将抓取下来的数据根据一定的规则进行提取
htmlElement = etree.HTML(text)
# 根据网页分析 得知第一个class='ui-slide-content' 的是正在热映的
ul = htmlElement.xpath("//ul[@class='ui-slide-content']")[0]
# print(etree.tostring(ul, encoding='utf-8').decode('utf-8'))

# 拿出当前ul标签中的 子li标签   注意：要加 .
lis = ul.xpath("./li")
movies = []
for li in lis:
    # 后面加 [0] 的原因： 取出第一个元素 ，而且 XPath返回的是一个列表，[0]可以变成一个对象
    title = li.xpath("@data-title")
    score = li.xpath("@data-rate")
    director = li.xpath("@data-director")
    actors = li.xpath("@data-actors")
    region = li.xpath("@data-region")
    # 在这个li标签中只有一个 img标签
    poster = li.xpath(".//img/@src")
    # 封装成一个字典
    movie = {
        'title': title,
        'sore': score,
        'director': director,
        'actors': actors,
        'region': region,
        'poster': poster
    }
    movies.append(movie)

print(movies)