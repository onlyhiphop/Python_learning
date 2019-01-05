"""
    Discuz论坛的爬取
"""
from lxml import etree
import requests
from urllib import parse
import csv


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/64.0.3282.167 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        if "抱歉，指定的主题不存在或已被删除或正在被审核" in resp.text:
            return False
        return resp.text
    else:
        return False


def parse_url(url):
    html_doc = get_html(url)
    htmlElement = etree.HTML(html_doc)
    # 获取帖子标题ml/head/title/text()")[0]
    # 获取帖子对应的url，从中取出tid，
    #     title = htmlElement.xpath("/ht帖子的id
    url = htmlElement.xpath("/html/head/link[1]/@href")[0]  # 第一个link标签
    tid = parse.parse_qs(url)['tid'][0]  # 输出 {'http://114.112.74.138/forum.php?mod': ['viewthread'], 'tid': ['5687']}
    # 获取这个帖子下所有人的 username 和 uid
    userlist = get_userlist(htmlElement)
    # 获取这个帖子下所有的回复 tid 和 内容
    contents = get_contents(htmlElement)
    # 封装里面所有回复人的uid，username，内容content，tid
    comments = get_comments(userlist, contents)
    # 封装一个帖子下的所有数据
    page = {
        "uid": userlist[0]['uid'],
        "author": userlist[0]['username'],
        "url": url,
        "title": title,
        "tid": tid,
        "content": str(comments[0]['content']),
        "comments": comments
    }
    return page
    # print(page)
    # print("=="*30)


# 将 userlist和contents整合 ，他们一一对应
def get_comments(userlist, contents):
    comments = []
    page_list = zip(userlist, contents)
    for index, page in enumerate(page_list):
        uid = page[0]['uid']
        username = page[0]['username']
        tid = page[1]['tid']
        content = page[1]['content']
        comments.append({
            "uid": uid,
            "username": username,
            "tid": tid,
            "content": content
        })
    return comments


# 获取td下的所有内容 ， 返回的封装的 tid content
def get_contents(htmlElement):
    contents = []
    tds = htmlElement.xpath('//td[@class="t_f"]')
    for td in tds:
        # print(etree.tostring(content, encoding='utf-8').decode('utf-8'))
        postmagess_id = td.xpath('./@id')[0]
        # 截取id
        postmagess_id = postmagess_id.split("_")[1]
        # 获取td下所有的文本
        content = td.xpath('.//text()')
        # 去掉特殊字符和空格等
        content = list(map(lambda string: string.strip().replace(',', '，'), content))

        contents.append({"tid": postmagess_id, "content": content})
    return contents


# 获得一个帖子下的所有  用户信息 ， 返回userlist 封装了 uid username
def get_userlist(htmlElement):
    userlist = []
    authi_all = htmlElement.xpath('//div[@class="authi"]')
    for index, i in enumerate(authi_all):
        if index % 2 == 0:
            a = i.xpath("./a/@href")[0]
            username = i.xpath("./a/text()")[0]
            uid = parse.parse_qs(a)['uid'][0]
            userlist.append({'uid': uid, 'username': username})
    return userlist


def main(max_tid):
    pages = []
    url = 'http://114.112.74.138/forum.php?mod=viewthread&tid='
    for i in range(5685, max_tid):
        url2 = url + str(i)
        pages.append(parse_url(url2))

    headers = ['uid', 'author', 'url', 'title', 'tid', 'content', 'comments']
    with open('discuz2.csv', 'w', encoding='utf-8', newline="") as fp:
        writer = csv.DictWriter(fp, headers)
        writer.writeheader()
        writer.writerows(pages)
    # with open('discuz2.csv','w', encoding='utf-8', newline='') as fp:
    #     for x in pages:
    #
    #         fp.write(x['uid'])
    #         fp.write('\t')
    #         fp.write(x['author'])
    #         fp.write('\t')
    #         fp.write(x['tid'])
    #         fp.write('\t')
    #         fp.write(x['content'][0])
    #         fp.write('\n')


if __name__ == '__main__':
    main(5687)
