"""
    CSS选择器：
        在 Tag 或 BeautifulSoup 对象的 .select() 方法中传入字符串参数,即可使用CSS选择器的语法找到tag
"""

text = """
<html>
<head>
    <title>The Dormouse's story</title>
    <style type="text/css">
        .box > p {   <!-- 直接子标签 -->
            background-color:red;
        }
    </style>
</head>
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

<div class = 'box'>
    <div class='no'>
        <p>第零行</p>
    </div>
    <p>第一行<p>
    <p>第二行<p>
    <p>第三行<p>
</div>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(text, "lxml")

# 1. 通过标签名查找
# 获取 title标签
soup.select("title")

# 1.2 通过标签 追层查找
# 获取 body下的 所有 div 标签 （这里返回两个对象）
soup.select("body div")

# 2. 通过类名查找
# 获取所有 class='sister' 的标签  返回列表
soup.select('.sister')

# 3. 通过id查找
# 获取所有 id = 'link1' 的标签
soup.select('#link1')

# 4. 组合查找 (用空格隔开)  （注意，前后也有追层查找的含义）
# 获取 所有 p 标签 id = link3 的内容
soup.select("p #link3")

# print(soup.select("div .no"))  # 找到的是第零行
# print(soup.select(".box div"))  # 找到了div[class='box']的对象 ， 如果div .box 获取的是[]
soup.select("div.box")   # 查找到了div中class 为box 的div标签

# 5. 直接子标签查找 ， 则使用 > 分隔
# 获取所有 类名为 .box 下直接子标签 p
soup.select(".box > p")

# 6. 通过属性查找 ， 属性需要用中括号括起来
# 获取 所有 a标签 并且 href 属性 为 http://example.com/elsie
soup.select("a[href='http://example.com/elsie']")


# 7. 获取所有 a标签下的 href属性
# aList = soup.select("a")
# for a in aList:
#     href = a['href']
#     print(href)

# 获取HTML中注释的字符串
text2 = """
    <p><!--我是注释的字符串--></p>
    <b>
        <!--我是不在一行的注释字符串-->
        <a href="www.baidu.com">百度</a>
    </b>
"""
soup2 = BeautifulSoup(text2, "lxml")
p = soup2.find("p")
print(p.string)   # 结果为：我是注释的字符串  Comment 类型:注释内容的类型

b = soup2.find("b")
print(b.string)  # 结果为None

# 总结：.string获取的只是一行字符，如果存在多行的话，就获取不到（多行存在 '\n' 字符）

# .contents 可以将tag的子节点以列表的方式
print(b.contents)

# .children 返回的是生成器
print(b.children)  # 输出一个生成器 （通过遍历这个生成器可以去到每一个值）
for bb in b.children:
    print(type(bb))

# 返回结果：['\n', '我是不在一行的注释字符串', '\n', <a href="www.baidu.com">百度</a>, '\n']


"""
    1. Tag: BeautifulSoup中所有的标签都是 Tag类型，并且 BeautifulSoup的对象其实本质上 也是一个Tag类型
            所有一些方法比如 find、find_all 并不是BeautifulSoup 的 而是 Tag  Tag是它的父类
    2. 
"""