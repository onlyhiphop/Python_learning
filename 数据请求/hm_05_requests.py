"""
    requests库：虽然Python标准库中urllib模块已经包含了我们平常使用的大多数功能，但是它的api使用起来让人
                感觉不太好，而Requests 使用更简洁方便

    安装： 利用pip         ：   pip install requests

    中文文档：http://docs.python-requests.org/zh_CN/latest/index.html
    github源码地址： https://github.com/requests/requests
"""
import requests


resp = requests.get('http://www.baidu.com/')

# .text 是python自己猜测的解码 ， 将bytes进行解码成str
# 所以可能出现乱码
# print(resp.text)
print(type(resp.text))  # str类型

# .content 是响应内容的 字节类型, 这个可以直接在网络和硬盘上传输
print(resp.content)
# 要准确的读取内容，自己去解码
print(resp.content.decode('utf-8'))

# .url 查看完整的url
print(resp.url)

# .encoding 查看响应头部字符编码
print(resp.encoding)

# .status_code 查看响应码
print(resp.status_code)

"""
    get请求方式：使用 params 传递参数
"""
params = {
    "wd": "中国"
}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/64.0.3282.167 Safari/537.36"
}
url = 'http://www.baidu.com/s'
response = requests.get(url=url, params=params, headers=headers)
print(response.url)  # url中有中文 ，requests中的params参数加进去后，它会自动帮你url编码

# 写入本地
with open('baidu.html', 'w', encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))

"""
    pose请求：利用 data 传递参数
"""
url2 = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
data = {
    'first': 'true',
    'pn': '1',
    'kd': 'python'
}
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/64.0.3282.167 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}
response2 = requests.post(url=url2, data=data, headers=headers2)

# 将返回的json字符串 变成字典形式
print(type(response2.json()))
