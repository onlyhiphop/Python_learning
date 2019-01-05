"""
    CSV文件：（Comma-Separated Values） 逗号分隔值，有时也称字符分隔值，因为分割字符也可以不是逗号
        1. 纯文本，使用某个字符集 比如 ASCII Unicode GB2312等

        2. 由记录组成（典型的是每行一条记录）

        3. 每条记录被分隔符分隔为字段（典型的分隔符有 逗号、分号、制表符（tab）、有时分隔符可以包括可选的空格）

        4. 每条记录都有同样的字段序列

    CSV文件处理：
        1. 读取CSV文件：csv.reader(fp)  返回一个迭代器
"""

import csv

"""
    读CSV文件
"""
# 1. 读取CSV文件： .reader() 返回迭代器，一行记录使用列表储存
def reader_csv_01():
    with open('text.csv', 'r', encoding='utf-8') as fp:
        reader = csv.reader(fp)
        next(reader)  # 让指针往下一位 ，后面就会从1开始遍历了
        for x in reader:
            print(x)  # 打印出来的是列表  一行记录就是一个列表


# 1.2 读取CSV文件：.DictReader() 返回迭代器，一行记录使用字典储存，字典的key就是标题行。
#                               迭代器里面不存在标题行
#  好处： 可以通过 key 去取对应的值
def reader_csv_02():
    with open('text.csv', 'r', encoding='utf-8') as fp:
        reader = csv.DictReader(fp)
        for x in reader:
            print(x['AGE'])



"""
    写CSV文件
    默认参数  delimitor=',' 可以自己改 ，但用Excel打开后格式不对应，只能用文本查看
"""
def write_csv_01():
    # 定义标题头
    headers = ['username', 'age', 'height']
    # 定义数据
    values = [('张三', 18, 160), ('李四', 19, 170), ('王五', 20, 180)]

    # newline参数设置为空， 如果不设置为空 默认是 \n 每写入一条数据都会在后面加上 \n  就会存在空行
    with open('text2.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.writer(fp)

        # 写入一行数据 .writerow()
        writer.writerow(headers)

        # 写入多行数据 .writerows()  参数是一个列表里面按规则存在 元组
        writer.writerows(values)


def write_csv_02():
    # 定义标题头
    headers = ['username', 'age', 'height']
    # 定义数据
    values = [
        {
            'username': '张三',
            'age': 18,
            'height': 160
        },
        {
            'username': '李四',
            'age': 19,
            'height': 170
        },
        {
            'username': '王五',
            'age': 20,
            'height': 180
        }
    ]
    with open('text2.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.DictWriter(fp, headers, delimiter='\t')
        # 注意 写入表头数据时要调用  .writeheader()
        writer.writeheader()

        # 写入列表 里面存的字典  的数据
        writer.writerows(values)


if __name__ == '__main__':
    write_csv_02()
