"""
    XPath(XML Path Language): 是一门在XML和HTML文档中查看信息的语言
                               可用来制作XML和HTML文档中对元素和属性进行遍历

    XPath开发工具：
        1. Chrome插件 XPath Helper
        2. Firefox插件 XPath Checker

    XPath语法：
        选取节点：( / : 获取子节点   // ：获取子孙节点)
            html             选取 HTML 节点
           /html/body/div    选取 HTML下的body下的所有div节点
           //div             选取整个网页下的 div 节点
           //div[@id]        选取整个网页下的拥有 id属性 的div 节点

        谓语：用来查找某个特定的节点或者包含某个指定的值的节点，被嵌在方括号中
            //div[1]          选取整个网页下 第一个 div节点 （下标从1开始，不是从0）
            //div[last()]     选取整个网页下 最后一个 div节点
            //div[position()<3]  选取整个网页下 前两个 div节点
            //div[@id=1]      选取所有 id = 1 的div节点
            //div[contains(@class,"f1")]  选取整个页面下 类名包含 f1 的div节点
            //a[@href]        选取所有 具有 href 的 a 标签
            //a/@href         选取所有 a 标签下 的href属性值
            //a/text()        选取所有 a 标签下的 文本
        通配符：
            * ：匹配任意字符
            @*：匹配节点中的任何属性

        选取多个路径：使用 “ 丨 ” 运算符
            //div[@class="top"]  |  //div[@class="bot"]

        运算符：> < == != <= >= * /
        or  and   mod(计算除法的余数)
        //div[@class="top" and @id="2"]  选取整个网页下 class=top 并且 id=2 的div节点
"""
import sys
# a = sys.argv[0]
# print(a)

# tup = (1, 2, 3)
# n1, n2, n3 = tup
# print(n1)


# def test(a):
#     if a == 0:
#         return " "
#     return 1
#
#
# if __name__ == '__main__':
#     if test(0):
#         print("false")
#     else:
#         print("true")

# a = 0 % 2
# print(a)

# a = ['i', 'am', '18']
# a = {"name": 'xiaoming', "uid": 18}
# # a = [1, 2, 3]
# print(''.join(a))
# a2 = [str(x) for x in a]
# print(a2)
# str1 = ''.join(a2)
# print(str1)
# str2 = ' '.join(a2)
# print(str2)

# a = '{{abdc}'
# a.replace('a', 'b')
# print(a)
# print(a.replace('{', 'b'))

# a = ['a', 'b']
# b = {"name": "xiaoming", "uid": 100}
# tt = str(a)
# dd = str(b)
# print(type(dd))

str = "abcdef"
print(str[1:-1])