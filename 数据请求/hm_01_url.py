"""
    urllib库：
        1. urlopen函数的使用
        2. urlretrieve 函数的使用
        3. urlencode 函数的使用
        4. parse_qs 函数的用法
        5. urlparse 函数的用法
        6. urlsplit 函数的用法
"""

from urllib import request
from urllib import parse

"""
     1. urlopen 函数的使用
         爬取了百度网页源代码  Ctrl + b 进入到 一个方法中
"""
"""
    参数：
        1. url：请求的url
        2. data：请求的data，如果设置了这个值，那么将变成post请求
        3. 返回值：返回值是一个http.client.HTTPResponse对象，这个对象是一个类文件句柄对象。
                   有  read(size) , read(line), read(lines), 以及 getcode 等方法。
"""
resp = request.urlopen('http://www.baidu.com')
# print(resp.read())  # read() 不带参数的话，默认读取全部
#
# print(resp.readline())  # 读取一行
#
# print(resp.getcode())   # 获取状态码  ： 200  400 ....


"""
    2. urlretrieve 函数的使用
        1> 方便的将网页上的一个文件保存到本地
"""
# 将网页上的 http://www.baidu.com 这个HTML文件下载到了当前的工作目录，并命名为 baidu.html
request.urlretrieve('http://www.baidu.com', 'baidu.html')

"""
    3. urlencode 函数的使用
        urlencode 可以把字典数据转换为 URL编码的数据。（编码后还是字符）
"""
data = {"name": "小明", "age": 18, "say": "hello  world!!"}
result = parse.urlencode(data)
print(result)

# urlencode 一个小实例用法
""" 错误：
    url = 'http://www.baidu.com/s?wd=刘德华'
    resp = request.urlopen(url)
    print(resp)
    正确：
    url = 'http://www.baidu.com/s'
    param = {"wd": "刘德华"}
    qs = parse.urlencode(param)
    url = url + '?' + qs
    resp = request.urlopen(url)
    print(resp)
"""

"""
    4. parse_qs 函数的用法
        可以将经过编码后的url参数进行解码
        返回一个字典
        
        一般用于获取url中的query部分 
        url = 'http://114.112.74.138/forum.php?mod=viewthread&tid=5687'
        parse_url = parse.urlparse(url)
        query = parse_url.query    # 值为：mod=viewthread&tid=5687
        tid = parse_qs(query)['tid'][0]  # {'mod': ['viewthread'], 'tid': ['5687']}
        
        parse_qsl(query)  返回的是一个列表 [('mod', 'viewthread'), ('tid', '5687')]
"""
result2 = parse.parse_qs(result)
print(result2)
"""
    5. urlparse 函数的用法  （对url中各个组成部分进行分割）
    6. urlsplit 函数的用法
        几乎相同的功能，urlparse 比 urlsplit 多返回一个 params 属性
        在 path /后面 ? 前面 的就是params值
"""
url = 'http://www.baidu.com/s;hello?wd=python&username=abc#1'  # 随便写的url
result = parse.urlparse(url)
# print(result)
# 输出结果
# ParseResult(scheme='http', netloc='www.baidu.com', path='/s', params='', query='wd=python&username=abc', fragment='1')

# print("scheme: %s" % result.scheme)
# print("netloc:"+ result.netloc)
# print('path:', result.path)
# print('query:', result.query)
# print(type(result.query))
# result2 = parse.urlsplit(url)
# print(result2)
