"""
    ProxyHandler处理器:
        设置一些代理服务器，每隔一段时间换一个代理，就算ip被禁止，依然可以换个ip继续爬取

    常用的代理有：
        西刺免费代理ip：http://www.xicidaili.com/
        快代理：http//www.kuaidaili.com/
        代理云： http://www.dailiyun.com/

        httpbin.org: 专门测试 你的http请求  通过它可以查看你的ip ，来验证你有没有代理成功

    1. 代理的原理：在请求目的网站之前，先请求代理服务器，然后让代理服务器去请求目的网站，
        代理服务器拿到目的网站的数据之后，再转发给我们的代码

"""
from urllib import request

# 不使用代理
url = 'http://httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read())

# 使用代理
# 1. 使用功能ProxyHandler ，传入代理构建一个 Handler
handler = request.ProxyHandler({"http": "58.53.128.83:3128"})
# 2. 使用上面创建的Handler 构建一个opener
opener = request.build_opener(handler)
# 3. 使用功能opener去发送一个请求
resp2 = opener.open(url)
print(resp2.read())