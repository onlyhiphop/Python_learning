"""
    BeautifulSoup4库：
        和lxml一样，Beautiful Soup 也是一个HTML/XML 的解析器，主要的功能也是如何解析和提取 HTML/XML 数据。
        lxml只会局部遍历，而BeautifulSoup 是基于HTML DOM的，会载入整个文档，解析整个DOM树，因此时间和内存
        开销都会大很多，所以性能要低于lxml。

        BeautifulSoup 用来解析HTML比较简单，api非常人性化，支持css选择器，Python标准库中的HTML解析器，也
        支持lxml 的XML解析器

        Beautiful Soup3 目前已经停止开发，推荐使用Beautiful Soup4

        中文文档： https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html

    几大解析工具的对比：
        BeautifulSoup    最慢     最简单
        lxml             快       简单
        正则             最快      最难

    解析器：
    Python标准库： BeautifulSoup(markup, "html.parser")     Python的内置标准库
                    执行速度适中  文档容错能力强

    lxml HTML 解析器： BeautifulSoup(markup, "lxml")    速度快 ，文档容错能力强 ，需要安装C语言库

    lxml XML 解析器：  BeautifulSoup(markup, ["lxml", "xml"])或BeautifulSoup(markup, "xml")
                        速度快，唯一支持XML的解析器，需要安装C语言库

    html5lib：   BeautifulSoup(markup, "html5lib")   最好的容错性，以浏览器的方式解析文档，生成HTML5格式的文档
                    速度慢 不依赖外部扩展
"""

from bs4 import BeautifulSoup, Tag

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title">
    <b>The Dormouse's story</b>
</p>
<p class="body">
    <b>long long ago</b>
    <b>have a cat</b>
    <b>is a very fat</b>
</p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1" class='bb'>Elsie</a>,
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>

<table>
    <tr>
     <td colspan="2">姓&nbsp;&nbsp;&nbsp;&nbsp;名</td>
     <td>&nbsp;</td>
     <td width="100px">职务</td>
     <td colspan="2" width="100px">&nbsp;</td>
     <td colspan="2" width="100px">出差事由</td>
     <td colspan="4">&nbsp;</td>
    </tr>
</table>
"""

# 第一个参数：一个网页的文本   第二个参数：解析器
soup = BeautifulSoup(html_doc, "lxml")

# 按照标准的缩进格式的结构输出:
# print(soup.prettify())

# 获取 title 标签
soup.title
# 获取 title 标签中的文本
soup.title.string

# 从文档中获取所有文字  返回的是一个字符串
soup.get_text()

# 获取所有的 a标签 ,参数limit：限制查询的次数  返回的是一个列表
soup.find_all('a', limit=2)

soup.find_all('a', limit=2)[1]
# 获取第二个 a标签 ，

"""
    注意 find_all() 返回的是一个列表 
         find() 返回的是一个对象 所以可以连用 soup.find('head').find('title')
"""
# 获取 第一个 id = link1 的标签
soup.find(id="link1")

# 获取所有 class = "sister" 的 a 标签  注意：因为class是关键字 ，所有这里的参数有个 下划线 _

soup.find_all('a', class_='sister')  # 返回一个列表

soup.find_all('a', attrs={'class': 'sister'})

# 获取 id = 'link1' 并且 class = 'sister'
soup.find_all('a', attrs={'id': 'link1', 'class': 'sister'})

# 获取所有 a标签 的href属性
aList = soup.find_all('a')
for a in aList:
    # 1. 通过下标去获取
    href = a['href']
    # print(a.attrs)
    # print(href)
    # 2. 通过attrs属性方式
    href2 = a.attrs['href']
    # print(href2)


# 获取第二个到最后一个 a 标签
aL = soup.find_all('a')[1:]
aTow = aL[1]  # 取出列表中第二个
# print(aTow)  # 输出的是标签
# print(aTow.string)  # 输出标签中的文本

# 获取 a 标签中 所有的字符  tag.strings 获取一个标签中所有的字符 包括一些换行
# for a in aL:
#     print(list(a.strings))
#     for string in a.strings:
#         print(string)

# tag.stripped_strings 可以除去多余空白字符
# for a in aL:
#     for string in a.stripped_strings:
#         print(repr(string))    # repr : 加上 '' 号


"""
    所有标签对象 都叫 Tag 对象：
        1. 每个 Tag 都有自己的名字 ， 通过 .name 获取 (也就是标签的名称)
            如果改变了tag的name,那将影响所有通过当前Beautiful Soup对象生成的HTML文档
        2. 一个tag可能有很多个属性 ，tag的属性的操作方法与字典相同 
            a['href'] 取出其中一个属性，   .attrs 取出所有属性，返回的是一个列表
            tag的属性可以被添加,删除或修改.
        3.  .string 获取某个标签下的非标签字符串，返回来的是个字符串
                注意：如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None :
            .strings 获取tag 里面的所有子孙非标签字符串 （包括空白字符和换行），返回来的是个生成器 可以通过 list（） 转化成列表输出
            .stripped_strings   获取所有字符串 去掉空格和一些换行，返回来的是个生成器
            .get_text() 获取某个标签下的子孙非标签字符串，不是以列表的形式返回，是以普通字符串返回
"""
