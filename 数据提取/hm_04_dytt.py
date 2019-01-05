"""
    电影天堂爬取：使用lxml爬取
"""
# encoding: utf-8


from lxml import etree
import requests

BASE_DOMAIN = 'http://dytt8.net'


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/64.0.3282.167 Safari/537.36'
}


# 获取 一页中的 每一个电影的详情页 url
def get_detail_urls(url):
    resp = requests.get(url, headers=HEADERS)
    # print(resp.text)  # .text 按照它默认的方式解码   .content 是二进制格式，没有解码
    # 不是utf-8编码 出现错误UnicodeDecodeError  可以查看网页源码 查看编码
    # print(resp.content.decode('utf-8'))

    #  requests 只会简单地从服务器返回的响应头的 Content-Type 去获取编码，如果有 Charset 才能正确识别编码，
    #  否则就使用默认的 ISO-8859-1，这样一来某些不规范的服务器返回就必然乱码了。
    # print(resp.encoding)

    # requests 内部的 utils 提供了一个从返回 body 获取页面编码的函数，get_encodings_from_content
    # print(requests.utils.get_encodings_from_content(resp.text))

    # text = resp.content.decode('gbk')
    # print(resp.content.decode("gbk"))  # 网页上是 gb2312 用gbk编码
    # 也可以 text = resp.text.encoding('utf-8').decode('utf-8')  先编码 再解码
    text = resp.text   # 最好不去对它解码，这里只是去获取url
                       # 因为可能存在 不能用你设置的编码 去解码的字符 就会出现错误
                    # 最好的方式是 去对你需要的字符进行解码 ， 不要对整个页面进行解码

    htmlElement = etree.HTML(text)
    url_details = htmlElement.xpath("//table[@class='tbspan']//a/@href")
    # for ud in url_details:
    #     print(BASE_DOMAIN + ud)  # 发现取出的只是后半部分，需要加上你前半部分，定义一个全局变量 BASE_DOMAIN

    # map(function,iterable)
    # 函数的使用：遍历iterable ， 对其中的每一项经常 function 函数操作
    url_details = map(lambda url_last: BASE_DOMAIN+url_last, url_details)
    return url_details


# 获取
def page_urls():
    # 声明一个 movies 列表 存放每一部电影的字典
    movies = []

    base_url = 'http://dytt8.net/html/gndy/dyzz/list_23_{}.html'   # 发现只是后面 1 2 3 的改 到不同的页
    # 获取 1到2 页的url
    for num in range(1, 3):
        url = base_url.format(num)  # .format 可以加num 加入 {} 中
        url_details = get_detail_urls(url)   # 获取到每一页中每一部电影的 详情页的url
        # print(list(url_details))   # 将map转换成list输出
        for url_detail in url_details:  # detail_url 是 取出的 其中一部电影的详情页url
            # print(url_detail)
            # 返回一部电影详情页的各种信息 字典
            movie = parse_detail_url(url_detail)
            movies.append(movie)
            print(movies)


# 解析一部电影详情页
def parse_detail_url(detail_page_url):
    movie = {}
    resp = requests.get(detail_page_url, headers=HEADERS)
    text = resp.content.decode('gbk')    # 如果不去手动解码，自动解码会出现乱码错误，不利于后面的操作
    html = etree.HTML(text)

    # 获取电影的标题   返回原本是个列表，加上[0]上，就取出了里面的第一个元素，变成了对象
    title = html.xpath('//div[@class="title_all"]//font[@color="#07519a"]/text()')[0]
    # print(title)
    movie['title'] = title

    # 发现所有信息都在 div[@id="Zoom"] 下 ， 所以先去获取这个标签
    zoom = html.xpath('//div[@id="Zoom"]')[0]  # 必须 [0] 获取一个lxml对象，只有lxml对象才有xpath方法
    # print(type(zoom))

    # 获取电影的海报和截图
    poster = zoom.xpath('.//img/@src')[0]
    screenshot = zoom.xpath('.//img/@src')[1]
    # print(poster2)
    movie['poster'] = poster
    movie['screenshot'] = screenshot

    # 获取电影所有的详情信息
    infos = zoom.xpath('.//text()')  # 得到了所有的文本， 并以一行为一个元素 形成一个列表
    # 根据列表项去取相应的信息
    # enumerate() 函数  遍历 返回一个索引下标和对象元素  （函数内第二个参数可以设置从第几个下标开始，enumerate(infos,start=1)）
    for index, info in enumerate(infos):
        if info.startswith("◎年　　代"):  # .startswith() 是以什么开头的字符串
            info = parse_info(info, "◎年　　代")    # .strip() 去掉前后的空格
            # print(info)
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = parse_info(info, "◎产　　地")
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info, "◎类　　别")
            movie['category'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info, "◎片　　长")
            movie['time'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info, "◎导　　演")
            movie['director'] = info

        # 特殊的地方，主演有很多个 占了很多行， 所以在列表的不同项
        elif info.startswith("◎主　　演"):
            actors = []
            info = parse_info(info, "◎主　　演")
            actors.append(info)
            # 根据下标 遍历 取出其他演员
            for i in range(index+1, len(infos)):
                # 当碰到了简介时，说明 演员结束了
                if infos[i].startswith("◎简　　介"):
                    break
                actor = infos[i].strip()
                # print(actor)
                actors.append(actor)
            # print(actors)
            movie['actors'] = actors

        elif info.startswith("◎简　　介"):
            intro = infos[index+1].strip()
            # print(intro)
            movie['intro'] = intro

    # 获取下载地址
    download_url = zoom.xpath(".//td[@bgcolor='#fdfddf']/a/@href")
    movie['download_url'] = download_url
    return movie


# 去根据规则解析info
def parse_info(info, rule):
    return info.replace(rule, "").strip()


if __name__ == '__main__':
    page_urls()
