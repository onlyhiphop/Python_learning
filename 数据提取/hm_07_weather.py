"""
    中国天气网信息爬取：使用BeautifulSoup爬取
"""

import requests
from bs4 import BeautifulSoup

from pyecharts import Bar

ALL_DATA = []


def main():
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml'
    ]
    for url in urls:
        parse_pageurl(url)

    # .sort  key参数 按照里面的某个值 默认升序排序
    # lambda 表达式 ， 取出每个字典中的 min_temp 项
    ALL_DATA.sort(key=lambda data: data['min_temp'])

    # 取前十个
    data = ALL_DATA[0:10]
    # 可视化数据 pyecharts
    # map(func, list) 函数 返回的是一个map对象 需要变成list
    cities = list(map(lambda x: x['city'], data))
    min_temps = list(map(lambda x: x['min_temp'], data))

    chart = Bar('中国天气最低气温排行榜')
    chart.add('', cities, min_temps)
    chart.render('temperature.html')


def parse_pageurl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/64.0.3282.167 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    html_doc = resp.content.decode('utf-8')
    # print(html_doc)

    """
        因为 此处 港澳台页面 少了 /table 标签 lxml无法为其补充，所以会出现错误
        在浏览器上看好像有 /table 标签， 那是因为浏览器为其补充了 ， 查看源代码则没有
        html5lib： 可以以浏览器的方式解析文档
    """
    soup = BeautifulSoup(html_doc, "html5lib")
    conMidtab = soup.find('div', class_='conMidtab')  # find_all 返回的是列表  所以加 [0]取出对象
    tables = conMidtab.find_all('table')  # 取出所有表
    for table in tables:  # 遍历所有表
        trs = table.find_all('tr')[2:]
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')

            city_td = tds[0]
            min_temp_td = tds[6]
            if index == 0:
                city_td = tds[1]  # 返回的是一个Tag对象
                min_temp_td = tds[7]
            # 取出Tag里面的文本，  .stripped_strings 返回的是个生成器，list()将生成器转换成列表  [0]取出列表对象 str
            city = list(city_td.stripped_strings)[0]
            # print(type(city))   取出的city是 str类型
            min_temp = list(min_temp_td.stripped_strings)[0]
            # 转换成int类型 方便后面进行排序
            min_temp = int(min_temp)

            # print('city:', city, 'min_temp:', min_temp)
            ALL_DATA.append({'city': city, 'min_temp': min_temp})


if __name__ == '__main__':
    main()
