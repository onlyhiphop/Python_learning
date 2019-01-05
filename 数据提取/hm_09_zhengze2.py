"""
    1. 正则表达式的小案例
    2. 开始结束和或语法
"""
import re

"""
    1. 正则表达式的小案例
"""
# 1.验证手机号码
text = '18370447261'
# ret = re.match('1[38]\d{9}', text)
# print(ret.group())

# 2.验证邮箱
email = 'hynever123_@qq.com'
# ret = re.match('\w+@[a-z0-9]+\.com', email)
# print(ret.group())

# 3.验证URL
url = 'http://www.baidu.com'
ret = re.match('(http|https|ftp)://[^\s]+', url)
# print(ret.group())

# 4.验证身份证
personid = '360782199702197035'
ret = re.match('\d{17}[xX\d]', personid)
# print(ret.group())


"""
    2.开始结束和或语法
    .search() 在整个字符串中去查找
"""
# 匹配 以....开始 ： ^
start = 'hello'
ret = re.search('^he', start)
# print(ret.group())

# 匹配 以....结尾： $
over = 'xxxxa@163.com'
ret = re.search('\w+a(@163.com)$', over)
# print(ret.group())

# 匹配多个表达式或者字符串
orstr = 'http'
ret = re.match('ftp|https|http', orstr)
# print(ret.group())

"""
    贪婪模式：会匹配尽量多的字符，默认是贪婪模式
    非贪婪模式：会匹配尽量少的字符
"""
tl = '<h1>标题</h1>'
ret = re.match('<.+>', tl)   # 贪婪模式 会匹配到 <   h1>标题</h2   > 最后那个 > 尖括号里面的内容
ret2 = re.match('<.+?>', tl)
# print(ret.group() + '\n' + ret2.group())

# 匹配 0-100 之间的数字
# 不可以出现：09 101 1001等等
nub = '100'
ret = re.match('([1-9]\d?0?|0)$', nub)
ret2 = re.match('[1-9]\d?$|100$', nub)
# print(ret.group())
# print(ret2.group())