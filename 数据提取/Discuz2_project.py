"""
    bs4爬取Discuz论坛
"""

import requests
from bs4 import BeautifulSoup
from urllib import parse
import csv

def get_url_content(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        if "抱歉，指定的主题不存在或已被删除或正在被审核" in resp.text:
            return False
        else:
            return resp.text
    else:
        return False


def get_user_list(soup):
    userList = []
    authi = soup.select('.authi')
    for index, author in enumerate(authi):
        if index % 2 == 0:
            url = author.a['href']
            query = parse.urlparse(url).query
            uid = parse.parse_qs(query)['uid'][0]
            username = author.a.string
            userList.append({"uid": uid, "username": username})
    return userList


def get_contents_list(soup):
    comments = []
    tds = soup.select(".t_f")
    for td in tds:
        content = td.get_text().strip().replace('\n', '')
        postmessage_id = td['id'].split('_')[1]
        comments.append({"tid": postmessage_id, "content": content})
    return comments


def get_url(max_tid):
    pages = []
    u = 'http://114.112.74.138/forum.php?mod=viewthread&tid='
    for i in range(5600, max_tid):
        url = u + str(i)
        page = parse_url(url)
        pages.append(page)
    return pages


def parse_url(html_doc):

    soup = BeautifulSoup(html_doc, "html5lib")
    title = soup.title.string.strip()
    url = soup.link['href']
    parse_url = parse.urlparse(url)
    query = parse_url.query
    tid = parse.parse_qs(query)['tid'][0]
    userList = get_user_list(soup)
    author = userList[0]
    comments = get_contents_list(soup)

    for i in range(len(userList)):
        comments[i]['uid'] = userList[i]['uid']
        comments[i]['username'] = userList[i]['username']


    page = {
        "uid": author['uid'],
        "author": author['username'],
        "tid": tid,
        "url": url,
        "title": title,
        "content": comments[0]['content'],
        "comments": comments[1:]
    }
    return page


if __name__ == '__main__':
    max_tid = 6000
    u = 'http://114.112.74.138/forum.php?mod=viewthread&tid='
    file_data = open('discuz2.csv', 'w', encoding='utf-8')
    for i in range(1, max_tid):
        url = u + str(i)
        html_doc = get_url_content(url)
        if html_doc:
            page = parse_url(html_doc)
            comments = page['comments']
            comments_str = ''
            for onedata in comments:
                for key in onedata:
                    comments_str = comments_str + onedata[key] + '::'
                comments_str = comments_str[:-2]
                comments_str = comments_str + '##'
            comments_str = comments_str[:-2]
            print(comments_str)
            # comments = [str(x) for x in comments]
            # comments = '#'.join(comments)
            # comments = comments.replace('{', '').replace('}', '').replace(',', '-').replace('\'', '')
            data_line = "%s\t%s\t%s\t%s\t%s\t%s\t%s" % (
                page['uid'], page['author'], page['tid'], page['url'], page['title'], page['content'], comments_str
            )
            # uid  author  tid  url  title  content  comments
            # print(data_line)
            file_data.write(data_line + '\n')
        else:
            break


    file_data.close()


    # pages = get_url(5606)
    # headers = ['uid', 'author', 'tid', 'url', 'title', 'content', 'comments']
    # with open('discuz2.csv', 'w', encoding='utf-8', newline='') as fp:
    #     writer = csv.DictWriter(fp, headers, delimiter='\t')
    #     writer.writeheader()
    #     writer.writerows(pages)
    #
    # print(pages)
