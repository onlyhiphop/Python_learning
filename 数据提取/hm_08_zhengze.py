"""
    正则表达式
    1. 单个字符的匹配
    2. 多个字符的匹配
"""

import re

"""
    1. 单个字符的匹配
"""
# 1. 匹配某个字符串
text = 'hello'
# .match()  只会从开头去匹配字符  如果是 ahello 则会报错
# .serach() 从整个字符串中去取
ret = re.match('he', text)
ret2 = re.search('lo', text)
# # .group() 返回 匹配的结果
# print(ret.group())
# print(ret2.group())

# 2.匹配任意的一个字符： 点(.)
#  注意 不能匹配到 \n 换行符
textx = '\n'
ret = re.match('.', textx)
# print(ret.group())  # 会报错，因为匹配不到

# 3.匹配任意的一个数字（也就是0~9）： \d
text2 = '23'
ret = re.match('\d', text2)
print(ret.group())   # 2

# 4.匹配任意的非数字： \D

# 5.匹配空白字符（\n  \t  \r）： \s
text3 = '\n '
ret = re.match('\s', text3)
print(ret.group())  # 返回一个换行

# 6.匹配的是 a-z ，A-Z ，数字和下划线： \w

# 7. \W 和 \w 正好相反

# 8. [] 组合的方式，只要满足中括号中的其中一个字符就可以
text4 = '2'
# ret = re.match('[a02]', text4)
# print(ret.group())

# 8.1 []组合方式代替 \d   []里面的0-9代表 0到9
ret = re.match('[0-9]', text4)

# 9. 多个字符： +   匹配前面的格式 可以有一个或者多个
text5 = '0797-88888'    # \- 中的 \ 是转义
ret = re.match('[\d\-]+', text5)
print(ret.group())

# 8.2 取非 在前面加上(只有在中括号里面使用才是取非的意思)： ^
ret = re.match('[^0-9]', text4)  # 表示非 0到9的数字  想当于  \D

# 8.2.1 以...开始(不在中括号里面的)： ^
ret = re.match('^07', text5)   # 匹配以07开始的
print(ret.group())

# 8.3 []代替 \w
ret = re.match('[0-9a-zA-Z_]', text5)

# 8.4 []代替 \W
ret = re.match('[^0-9a-zA-Z_]', text5)


"""
    2. 多个字符的匹配
"""
# 1. 匹配任意多个字符(0或者任意多个)： *
# 写在规则后面 ， 如 \d* 匹配任意多个数字   \s* 匹配任意多个空白字符
text = 'adbc'
ret = re.match('\d*', text)
# print(ret.group())

# 2. 匹配一个或者多个字符： +
ret = re.match('\w+', text)
# print(ret.group())

# 3.匹配一个或者0个： ?
ret = re.match('\w?', text)
# print(ret.group())

# 4.匹配m个字符： {m}
ret = re.match('\w{2}', text)
# print(ret.group())

# 5.匹配m-n个字符：{m,n}   可以右边越界
ret = re.match('\w{1,5}', text)
# print(ret.group())

# 6.匹配 a 或 b 的字符： (a|b)
ret = re.match('(a|b)', text)
print(ret.group())