"""
    古诗文网的爬取：使用正则表达式爬取
"""
import requests
import re

def parse_url(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/64.0.3282.167 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    text = resp.text

    # re.DOTALL 可以取出全部字符  因为 . 不能匹配 \n  页面中存在很多\n
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</br>', text, re.DOTALL)
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    authors = re.findall(r'<p class=""source>.*?<a.*?>.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    content_tags = re.findall(r'<div class="contson" .*?>(.*?)</div>', text, re.DOTALL)
    contents = []
    for content in content_tags:
        x = re.sub(r'<.*?>', "", content)
        contents.append(x.strip())  # 去掉空白字符

    poems = []
    """
        zip函数： zip([iterable, ...])
        如： a = [1,2,3]
             b = [4,5,6]
             c = [4,5,6,7,8]
             zipped = zip(a,b)     # 打包为元组的列表
            [(1, 4), (2, 5), (3, 6)]
            
            zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
            [(1, 2, 3), (4, 5, 6)]
    """
    for value in zip(titles, dynasties, authors, contents):
        # 可以一一对应取出元组里面的值
        title, dynasty, author, content = value
        poem = {
            'title': title,
            'dynasty': dynasty,
            'author': author,
            'content': content
        }
        poems.append(poem)


def main():
    url = 'https://www.gushiwen.org/default_1.aspx'
    parse_url(url=url)


if __name__ == '__main__':
    main()
