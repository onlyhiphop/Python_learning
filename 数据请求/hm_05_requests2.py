"""
    1. 使用requests添加代理
    2. requests处理cookie信息
"""

import requests


"""
    1. 使用requests添加代理
"""
# proxy = {
#     'http': '183.15.172.23:61430'
# }
# url = 'http://httpbin.org/ip'
# resp = requests.get(url=url, proxies=proxy)
# print(resp.text)


"""
    2. requests处理cookie信息
"""
response = requests.get('http://www.baidu.com/')

# 获取cookie信息 .cookie   get_dict() 变成字典
print(response.cookies.get_dict())

"""
    session:一个会话
"""
headers3 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/64.0.3282.167 Safari/537.36',
}
data = {
    'email': '760003259@qq.com',
    'password': '123456'
}
# 请求的url
login_url = 'http://www.renren.com/PLogin.do'

# 创建一个会话 session
session = requests.session()
# 用这个session去登录， 就能把cookie信息存入session对象中
session.post(url=login_url, data=data, headers=headers3)

# 这时，session中已经有了cookie信息，所以再次去访问需要登录的页面 就能成功了
response = session.get('http://www.renren.com/968618975/newsfeed/origin')
with open('renren.html', 'w', encoding='utf-8') as fp:
    fp.write(response.text)


"""
    处理不信任的SSL证书：
        对于那些已经被信任的SSL证书的网站，使用requests直接可以正常的返回响应
        
        要去访问不被信任的SSL证书，需要加上 verfity = False
"""
response4 = requests.get('', verfity=False)
print(response4.content.decode('utf-8'))
