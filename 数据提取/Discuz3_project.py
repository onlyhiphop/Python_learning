import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import parse_qs


# 根据url请求网站并获取html文本


def get_url_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        if "抱歉，指定的主题不存在或已被删除或正在被审核" in response.text:
            return False
        else:
            return response.text
    else:
        return False


def get_post_content_list(post_soup_object):
    content_object_list = post_soup_object.select('.t_f')
    content_list = []
    for i in range(len(content_object_list)):
        # 发帖id
        print(i)
        post_message_id = content_object_list[i]['id']
        tid = post_message_id.split("_")[1]
        content = content_object_list[i].string
        content_list.append({"tid": tid, "content": content})
    return content_list


def get_post_userlist(post_soup_object):
    user_info_doms = post_soup_object.select(".authi")
    user_list = []
    user_name = user_info_doms[0].a.string
    uid = parse_qs(user_info_doms[0].a['href'])['uid'][0]
    user_list.append({"user_name": user_name, "uid": uid})
    return user_list


def parse_post_data(html_text):
    soup_object = BeautifulSoup(html_text, "html5lib")
    # 获取title
    title = soup_object.title.string
    url = soup_object.link['href']
    parsed_url = urlparse(url)
    query_string_object = parse_qs(parsed_url.query)
    tid = query_string_object['tid'][0]
    user_list = get_post_userlist(soup_object)
    content_list = get_post_content_list(soup_object)
    for i in range(len(content_list)):
        content_list[i]["user_info"] = user_list[i]
    post_content_info = {
        "title": title,
        "url": url,
        "tid": tid,
        "author": user_list[0],
        "content": content_list[0]["content"],
        "comments": content_list[1:]
    }

    return post_content_info


# test
# content1 = get_url_content("http://114.112.74.138/forum.php?mod=viewthread&tid=1")
# parsed_post_content_info = parse_post_data(content1)
# print(json.dumps(parsed_post_content_info))
# print(content1)


# outer args
max_id = sys.argv[0]
max_id = 50
base_url = "http://114.112.74.138/forum.php?mod=viewthread&tid="
file = open("data.csv", "w", encoding='utf-8')
for i in range(1, int(max_id+1)):
    post_url = base_url + str(i)
    print(post_url)
    page = get_url_content(post_url)
    if page:
        parsed_post_data = parse_post_data(page)
        print(parsed_post_data)
        data_line = '%s,%s,%s,%s' % (parsed_post_data.get("tid"),
                                     parsed_post_data.get("title").replace(",", "%2C"),
                                     parsed_post_data["author"]["uid"],
                                     parsed_post_data.get("author").get("user_name"))
        print(data_line)
        file.write(data_line+"\n")
    else:
        print("false")
file.close()
