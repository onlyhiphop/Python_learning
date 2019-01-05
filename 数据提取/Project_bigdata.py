
# 使用urlparse包中的urlparse方法来解析url
# 主要用于分析URL中query组件的参数，返回一个key-value对应的字典格式
# 这句语句告诉Python，我们想要使用这个模块。sys模块包含了与Python解释器和它的环境有关的函数。
import sys
from urllib.parse import parse_qs
from urllib.parse import urlparse

import requests
# 引入request库， requests是python实现的简单易用的HTTP库，使用起来比urllib简洁很多
from bs4 import BeautifulSoup
# BS4本身是一种对描述语言进行封装的函数操作模块，通过提供面向对象的操作方式将文档对象中的
# 各种节点、标签、属性、内容等等都封装成了python中对象的属性，在查询操作过程中，通过调用指定的函数直接进行数据匹配检索操作，非常的简单非常的灵活。


# 判断"抱歉，指定的主题不存在或已被删除或正在被审核"是否在response.text网页源码（文本形式）中(是，返回False，否，以文本形式返回网页源码)
def get_url_content(url):
    response = requests.get(url)
    # 请求访问目标网站
    if response.status_code == 200:
        # 判断请求状态码（状态），返回值为200正常。
        if "抱歉，指定的主题不存在或已被删除或正在被审核" in response.text:
            return False
        else:
            return response.text
    else:
        return False


def parse_post_data(html_text):
    soup_object = BeautifulSoup(html_text, "html5lib")
    # 解析网页源码
    title = soup_object.title.string
    # 获取title并转换成string类型
    url = soup_object.link['href']
    # 获取href后的链接里的内容
    parsed_url = urlparse(url)
    # 将url解析成6个部分（协议、位置、路径、参数、查询、片段）
    query_string_object = parse_qs(parsed_url.query)
    # 获取解析后元组中的query项
    tid = query_string_object['tid'][0]
    # 获取解析后元组中第一个tid，代表着发帖
    user_list = get_post_userlist(soup_object)
    content_list = get_post_content_list(soup_object)
    for i in range(len(content_list)):
        content_list[i]["user_info"] = user_list[i]
    # 获取发帖用户
    post_content_info = {
        "title": title,
        "url": url,
        "tid": tid,
        "author": user_list[0],
        "content": content_list[0]["content"],
        "comments": content_list[1:]
    }
    return post_content_info


# 将抓取的数据以字典的形式保存
def get_post_content_list(post_soup_object):
    content_object_list = post_soup_object.select('.t_f')
    # 选择器。源码中标有.t_f的为获取对象
    content_list = []
    # 定义一个空列表
    for i in range(len(content_object_list)):
        postmessage_id = content_object_list[i]['id']
        # 获取发帖id
        tid = postmessage_id.split("_")[1]
        # 获取发帖ID，以"_"进行切分，取第二个元素
        content = content_object_list[i].string
        # 将下角标为i的数据转换为string类型
        content_list.append({"tid": tid, "content": content})
    return content_list


# 向列表中添加元素
def get_post_userlist(post_soup_object):
    user_info_doms = post_soup_object.select(".authi")
    # 选择器，可以获得多条也可以获得单条数据
    user_list = []
    # 定义一个用户空列表
    for i in range(len(user_info_doms)):
        if i % 2 == 0:
            user_name = user_info_doms[i].a.string
            # 将下角标为i的数据转换为string类型
            uid = parse_qs(user_info_doms[i].a['href'])['uid'][0]

            user_list.append({"user_name": user_name, "uid": uid})
    # 向列表中添加元素
    return user_list


content = get_url_content("http://114.112.74.138/forum.php?mod=viewthread&tid=5656")

# 调用get_url_content方法，请求"http://114.112.74.138/forum.php?mod=viewthread&tid=5656"，以文本形式返回网页源码
parsed_post_content_info = parse_post_data(content)
# 调用parse_post_data方法
# print(json.dumps(parsed_post_content_info))
# print(content)
# parse_post_data(get_url_content("http://192.168.15.122/forum.php?mod=viewthread&tid=5656"))
max_tid = 10
# max_tid = sys.argv[1]
# sys.argv实现从程序外部向程序传递参数
post_base_url = "http://114.112.74.138/forum.php?mod=viewthread&tid="
for i in range(1, max_tid):
    ret = get_url_content(post_base_url + str(i))
    # 调用get_url_content方法请求目标网站
    if ret:
        parsed_post_data = parse_post_data(ret)
        print("got post data,tid:%s" % (parsed_post_data["tid"]))
    else:
        print("tid:%s not found,continue" % i)



