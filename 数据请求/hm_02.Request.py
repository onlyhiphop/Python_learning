""""
    request.Request类：
        在请求的时候增加一些请求头
"""
from urllib import request, parse

# 使用 urlopen和 Request的区别   : 以下是拉勾网的url  拉勾网做了反爬虫
url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='

resp = request.urlopen(url)
# print(resp.read())


# User-Agent 是从 Chrome network信息下有
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 '
                  'Safari/537.36 ',
    
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}

# 得到Request对象
req = request.Request(url, headers=headers)
resp = request.urlopen(req)
# print(resp.read())


# 爬取搜索到的职位信息  比如：python
# 由于它做了反爬虫， 职位信息不在网页源代码中，是利用 js 追加到HTML中，所以信息不在此 url请求中
# 可以在 name中 找 position...json 找到真正的url

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

# 在Headers下面列表中看到了 其他data  所以传入 data
data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}
# 还看到了是 Post请求
req = request.Request(url, headers=headers,
                      data=parse.urlencode(data).encode('utf-8'),
                      method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
# 报错：TypeError: can't concat str to bytes  说明data是url传值，没有经过编码 parse.urlencode()
# 报错：POST data should be bytes, an iterable of bytes,
#       or a file object. It cannot be of type str.    post请求 是字节流 .encode('utf-8')
# 提示： 操作太频繁 （输出也要解码） 不是操作频繁 而是被识别出来了是爬虫，所以要再伪造真一点的请求头加上 Referer

