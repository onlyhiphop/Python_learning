"""
    JSON支持数据格式：
        1. 对象（对应python中的字典）：使用{}
        2. 数组（对应python中的列表）：使用[]
        3. 整形，浮点型，布尔类型，null类型。
        4. 字符串类型（字符串必须要用双引号不能用单引号）。

        多个数据之间使用逗号隔开。
        本质就是一个字符串。


    python对象转换成json字符串:
        1. .drumps()函数
        2. .drump()函数

    注意：因为json在dump的时候，只能存放ascii的字符，因此会将中文进行转义，这时候我们用 ensure_ascii 关闭这个特性

    在python中，只有基本数据类型才能转换成json格式的字符串 即：int float str list dict tuple

    json字符串load成python对象:
        1. .loads() 函数
        2. .load()函数
"""
import json

persons = [
    {
        'username': '张三',
        'age': '18',
        'country': 'china'
    },
    {
        'username': '李四',
        'age': '19',
        'country': 'USA'
    }
]

# 注意：如果含有中文, 必须将 ensure_ascii = False
# 因为，它默认对数据进行 Unicode 编码
persons_json = json.dumps(persons, ensure_ascii=False)

print(type(persons_json))   # str 类型
print(persons_json)   # 会发现 输出的都变成了 双引号

# 写在本地文件中
# with open('persons.json', 'w', encoding='utf-8') as fp:
#     fp.write(persons_json)


# 2. .drump()的使用
# with open('persons2.json', 'w') as fp:
#     json.dump(persons, fp)


"""
    json字符串转成python对象
"""
json_str = '[{"username": "张三", "age": "18", "country": "china"}, {"username": "李四", "age": "19", "country": "USA"}]'

# .loads() 函数
# persons = json.loads(json_str)
# print(type(persons))
# print(persons)

# .load() 函数
# with open('persons2.json', 'r') as fp:
#     persons = json.load(fp)
#     print(type(persons))
#     print(persons)
