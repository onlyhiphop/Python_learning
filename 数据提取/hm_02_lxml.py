"""
    lxml库：
        lxml是一个HTML/XML 的解析器，主要的功能是如何解析和提取HTML/XML 数据
        lxml和正则表达式一样，也是用C实现的，是一款高性能的Python HTML/XML 解析器

        官方文档： http://lxml.de/index.html
"""
from lxml import etree

text = """
    <!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <table border="1" width="800px" height="450px" style="text-align: center;">
            <tr>
                <td colspan="2">姓&nbsp;&nbsp;&nbsp;&nbsp;名</td>
                <td>&nbsp;</td>
                <td width="100px">职务</td>
                <td colspan="2" width="100px">&nbsp;</td>
                <td colspan="2" width="100px">出差事由</td>
                <td colspan="4">&nbsp;</td>
、
            </tr>
            <tr>
                <td width="50px">起日</td>
                <td width="50px">止日</td>
                <td width="100px">起讫地点</td>
                <td width="100px">项&nbsp;&nbsp;&nbsp;&nbsp;目</td>
                <td width="50px">张数</td>
                <td colspan="3" width="150px">金&nbsp;&nbsp;&nbsp;&nbsp;额</td>
                <td width="100px">项&nbsp;&nbsp;&nbsp;&nbsp;目</td>
                <td width="50px">天数</td>
                <td colspan="2" width="150px">金&nbsp;&nbsp;&nbsp;&nbsp;额</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>火车费</td>
                <td>&nbsp;</td>
                <td colspan=2"" width="100px">&nbsp;</td>
                <td width="50px">&nbsp;</td>
                <td>途中补助</td>
                <td>&nbsp;</td>
                <td >&nbsp;</td>
                <td width="50px">&nbsp;</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>汽车费</td>
                <td>&nbsp;</td>
                <td colspan=2"">&nbsp;</td>
                <td>&nbsp;</td>
                <td>住勤补助</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>室内交通费</td>
                <td>&nbsp;</td>
                <td colspan=2"">&nbsp;</td>
                <td>&nbsp;</td>
                <td>夜间乘车</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>住宿费</td>
                <td>&nbsp;</td>
                <td colspan=2"">&nbsp;</td>
                <td>&nbsp;</td>
                <td>其&nbsp;&nbsp;&nbsp;&nbsp;它</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>邮电费</td>
                <td>&nbsp;</td>
                <td colspan=2"">&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td colspan="2">小&nbsp;&nbsp;&nbsp;&nbsp;计</td>
                <td colspan="2">&nbsp;</td>
                <td>&nbsp;</td>
                <td colspan="2">小&nbsp;&nbsp;&nbsp;&nbsp;计</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td colspan="3">合&nbsp;&nbsp;&nbsp;&nbsp;计</td>
                

                <td colspan="9">(大写)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;仟&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;佰&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;拾 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;元&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;角&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;分 &nbsp;&nbsp;¥</td>
                
            </tr>
        </table>
    
"""


# .HTML() 会对这个文本 进行一些格式的补充  比如 </body>  </html>
def parse_text():
    htmlElement = etree.HTML(text)  # 返回一个Element对象, 默认使用HTML解析器，解析这个文本
    # etree.tostring() 能将Element转换成字符串
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))


def parse_file():
    # 会报错，lxml.etree.XMLSyntaxError: Opening and ending tag mismatch
    # 可能有一些网页标签不规范 ，而 .parse() 不会对网页进行一些补充， 这个方法默认使用xml解析器
    # htmlElement = etree.parse("lagou.html")   # .parse() 不会进行补充
    # print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))

    # 定义一个HTML解析器
    parser = etree.HTMLParser(encoding='utf-8')
    # 传入解析器
    htmlElement = etree.parse("lagou.html", parser=parser)
    # print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))

# """
#     .xpath() 的使用:  参数里面写 XPath语法
#         返回的是一个列表
# """
    # 获取所有的 div标签 .xpath()
    divs = htmlElement.xpath("//div")
    # for div in divs:
        # print(etree.tostring(div, encoding='utf-8').decode('utf-8'))

    # 获取第二个 div 标签 第一个元素
    div2 = htmlElement.xpath("//div[2]")[0]
    # for div22 in div2:
    #     print(etree.tostring(div22, encoding='utf-8').decode('utf-8'))

    # 获取 class=company 的div标签
    classes = htmlElement.xpath("//div[@class='company']")
    # for cla in classes:
    #     print(etree.tostring(cla, encoding='utf-8').decode('utf-8'))

    # 获取所有 a 标签下 href 属性值
    href = htmlElement.xpath("//a/@href")
    # for hf in href:
    #     print(hf)   # 输出的是值，不是列表 所有不用 tostring

    # 获取所有职位
        # 获取大于3的li
    li = htmlElement.xpath("//li[position()>3]")
    industry_list = []
    for lili in li:
        # 获取li标签中的第一个div  # .//div 代表当前标签内所有孙节点的div , 如果不加 点 就会是整个页面的 div 了
        div = lili.xpath(".//div[@class='industry']")
        # text() 获取到 该节点下的所有文本
        text = lili.xpath(".//div[@class='industry']/text()")
        print(div)
        print(text)

        # 可以创建一个字典存放
        industry = {
            'div': div,
            'text': text
        }
        industry_list.append(industry)


if __name__ == '__main__':
    parse_file()
