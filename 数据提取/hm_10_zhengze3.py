"""
    转义字符的匹配
    原生字符串: \n \t \r\n
"""
import re

"""
    转义字符的匹配
"""
# 对于特殊字符 使用 \ 进行转义匹配
info = 'apple price is $200'
ret = re.search('\$\d+', info)
# print(ret.group())

"""
    原生字符串: 
        1. 加上 \ 可以消除后面的 \ 的转义含义
        2. 在字符前面加个 r 代表原生的意思
        
    要匹配到字符里面的 \ 必须写连续四个 \ 
        因为在python中 \ 是转义字符 ， 在正则表达式中 \ 也是转义字符
"""
text = '\\n'
text2 = r'\n'
# print(text)
# print(text2)

# 提取出里面的 \
ret = re.match('\\\\n', text)
# 在python这一层中 加了 r 相当于传入 \\n 字符串，\ 不在有特殊含义，只要正则中进行对 \ 转义
ret2 = re.match(r'\\n', text)
print(ret.group())
print(ret2.group())
