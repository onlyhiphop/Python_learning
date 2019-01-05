"""
爬取Discuz论坛
"""
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import parse_qs
import csv

def get_url_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/64.0.3282.167 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        if "抱歉，指定的主题不存在或已被删除或正在被审核" in resp.text:
            return False
        else:
            return resp.text
    else:
        return False
    html_doc = resp.text


def get_user_list(soup):
    tag_authi = soup.select(".authi")
    user_list = []
    for index, authi in enumerate(tag_authi):
        if index % 2 == 0:
            username = authi.a.string
            url = authi.a['href']
            uid = parse_qs(urlparse(url).query)['uid'][0]
            user_list.append({"uid": uid, "username": username})
    return user_list


def get_comments_list(soup):
    comments_list = []
    tds = soup.select(".t_f")
    for td in tds:
        pid = td['id']
        pid = pid.split("_")[1]
        # content = list(td.strings)[0]
        content = td.text.strip().replace('\n', '')
        comments_list.append({"pid": pid, "content": content})
    return comments_list


def parse_url(html_doc):
    soup = BeautifulSoup(html_doc, 'html5lib')
    title = soup.title.string
    url = soup.link['href']
    tid = parse_qs(urlparse(url).query)['tid'][0]
    user_list = get_user_list(soup)
    comments_list = get_comments_list(soup)
    for i in range(len(comments_list)):
        comments_list[i]['uid'] = user_list[i]['uid']
        comments_list[i]['username'] = user_list[i]['username']

    page = {
        "uid": user_list[0]['uid'],
        "username": user_list[0]['username'],
        "tid": tid,
        "title": title,
        "url": url,
        "content": comments_list[0]['content'],
        "comments": comments_list[1:]
    }
    return page


u = 'http://114.112.74.138/forum.php?mod=viewthread&tid='
max_tid = 5662

# file = open(r'D:/discuztest.txt', 'w', encoding='utf-8')
pages = []
for i in range(5656, max_tid):
    url = u + str(i)
    html_doc = get_url_content(url)
    if html_doc:
        page = parse_url(html_doc)
        pages.append(page)
        # page = parse_url(html_doc)
        # data_line = "%s\t%s\t%s\t%s\t%s\t%s\t%s" % (
        #     page["uid"], page["username"], page["tid"], page["title"], page["url"], page["content"],
        #     page["comments"]
        # )
        # file.write(data_line + '\n')
    else:
        print("false")
# file.close()
headers = ["uid", "username", "tid", "title", "url", "content", "comments"]
with open(r'D:/discuztest.txt', 'w', encoding='utf-8', newline='') as fp:
    writer = csv.DictWriter(fp, headers, delimiter='\t')
    writer.writeheader()
    writer.writerows(pages)
