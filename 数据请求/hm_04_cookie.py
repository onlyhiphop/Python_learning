"""
    cookie格式：（chrom 下header可以看到）
    Set-Cookie:NAME=VALUE;Expires/Max-age=DATE;Path=PATH;Domain=DOMAIN_NAME;SECURE
        NAME: cookie的名字
        VALUE: cookie的值
        Expires: cookie的过期时间
        PATH: cookie作用的路径
        Domain：cookie作用的域名
        SECURE:是否只在https协议下起作用
"""
# from urllib import request, parse
# from http.cookiejar import CookieJar
#
# # 不使用cookie去请求 一个需要登入的页面 eg：http://www.renren.com/
# ren_url = 'http://www.renren.com/968618975'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/64.0.3282.167 Safari/537.36',
#     'Referer': 'http://zhibo.renren.com/top',
#     'Cookie': 'jo8kjexd-bglufz; depovince=ZGQT; _r01_=1; JSESSIONID=abclI5MNHJx9z_jz8sZBw; '
#               'ick_login=3de8c456-cdf1-4529-8b31-ef67fe15cb6a; t=1dc356e7ef39fecdda9828eecc7c51d85; '
#               'societyguester=1dc356e7ef39fecdda9828eecc7c51d85; id=968618975; xnsid=cb36832; '
#               'jebecookies=5fb01b84-20ba-4447-b714-6caf412bcab8|||||; '
#               'jebe_key=ef97aac7-a25f-4e1a-9e06-8b3354ab1563%7Caa2dd5a07fd0ec97f7e26f3ed4e97e48%7C1541680191671%7C1'
#               '%7C1541680193296; wp_fold=0; ver=7.0; loginfrom=null '
# }
# req = request.Request(url=ren_url, headers=headers)
# resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))  # resp.read() 取出来是一个bytes类型  bytes --> decode --> str
# # 将爬取的数据写成一个HTML文件写入本地
# # with open('renren.html','w',encoding='utf-8') as fp:
# #     # write 函数必须写入一个str的数据类型
# #     fp.write(resp.read().decode('utf-8'))
# # 最后打开的是一个登入页面，说明被拦截跳转到了登入页面
#
# """
#     1. 自己造一个cookie：利用Chrome抓包， 查看浏览器发送给服务器的cookie信息
#                     可以在Header 中看到cookie信息，所以我们也要放入header中
# """
#
#
#
# """
#     2. 可以走一遍登入的接口，然后，会自动形成一个cookie
#
#         使用到http.cookiejar模块
#         该模块主要的类有 CookieJar、FileCookieJar、 MozillaCookieJar、LWPCookieJar
#         CookieJar：管理HTTP cookie值、存储HTTP请求生成的cookie，向传出的HTTP请求添加cookie对象，
#                     整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失
#         FileCookieJar(filename, delayload=None,policy=None)：
#                    从CookieJar派生而来，用来创建FileCookieJar实例，检索cookie信息并将cookie存储到文件中
#                     filename是存储cookie的文件名，delayload为True时支持延迟访问文件，即只有在需要时才读取文件或在文件中共存储数据
#         MozillaCookieJar(filename, delayload=None,policy=None)：从FileCookieJar派生而来，创建与Mozilla浏览器cookie.txt兼容
#                                                                 的fileCookieJar实例
# """
# # 1. 登录
# # 1.1 创建一个CookieJar对象
# cookiejar = CookieJar()
# # 1.2 使用CookieJar对象 创建一个 HTTPCookieProcess对象
# handler = request.HTTPCookieProcessor(cookiejar)
# # 1.3 使用上一步创建的对象handler 创建一个opener
# opener = request.build_opener(handler)
# # 1.4 使用opener 发送登录的请求（人人网的邮箱和密码）
# headers2 = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/64.0.3282.167 Safari/537.36',
# }
# data = {
#     'email': '760003259@qq.com',
#     'password': '123456'
# }
# # 请求的url
# login_url = 'http://www.renren.com/PLogin.do'
# req = request.Request(login_url,
#                       # 先将data变成url编码字符，然后再变成字节
#                       data=parse.urlparse(data).encode('utf-8'),
#                       headers=headers2
#                       )
# # 不需要去接受它的返回，这里的目的是为了去获得它生产的cookie
# opener.open(req)
#
# # 2. 访问主页
# index_url = 'http://www.renren.com/968618975/newsfeed/origin'
#
# # 这时 CookieJar对象中就有了cookie信息，也就是说 opener已经有了cookie信息了
# req = request.Request(url=index_url, headers=headers2)
# resp = opener.open(req)
# # 把结果写到本地文件中
# with open('renren_login.html', 'w', encoding='utf-8') as fp:
#     fp.write(resp.read().decode('utf-8'))


"""
    MozillaCookieJar：
"""
from urllib import request
from http.cookiejar import MozillaCookieJar

# 创建一个cookieJar对象 , 命名这个cookie在本地保存的名字
cookiejar2 = MozillaCookieJar('cookie.txt')
# 创建一个HTTPCookieProcessor 对象
handler2 = request.HTTPCookieProcessor(cookiejar2)
# 创建一个opener对象
opener2 = request.build_opener(handler2)

# 去打开一个网页 , cookie信息就会存到 cookie对象中
resp = opener2.open('http://httpbin.org/cookies/set?course=abc')

# 将cookie对象保存到本地
# 有些cookie信息会在浏览器关闭的时候过期，上面请求后，就过期了，所以加上参数
cookiejar2.save(ignore_discard=True)

# 加载保存在本地的 cookie文件
cookiejar2.load(ignore_discard=True)
for cookie in cookiejar2:
    print(cookie)
