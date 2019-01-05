"""
    1. Series 一维，带标签数组
    2. DataFrame 二维，Series容器
"""
import pandas as pd
import string

"""
    创建Series
"""
# 1. 参数为列表时 ，默认是从0开始的索引
t2 = pd.Series([1, 2, 35, 15, 65])
print(type(t2))  # pandas.core.series.Series
print(t2)

# index 和 列表要一一对应 否则会报错
t3 = pd.Series([1, 2, 65, 55], index=list("abcd"))
print(t3)


# 2. 参数为字典  , 索引会直接是字典的key
temp_dict = {"age": 18, "name": "liao"}
t4 = pd.Series(temp_dict)
print(t4)
print(t4.dtype)  # 输出object

a = {string.ascii_uppercase[i]: i for i in range(10)}
print(a)

# index 这个时候取 a中key为inex的value匹配，如果没有对应的value 则为Nan
# 注意：如果出现了Nan，它会自动转化为 float类型
a2 = pd.Series(a, index=list(string.ascii_uppercase[5:15]))
print(a2)
print(a2.dtype)

"""
    2. 对Series对象的操作
"""
person_dict = {
    "age": 18,
    "name": "zhangsan",
    "sex": 1
}
p = pd.Series(person_dict)

# 1. 既可以通过key来取值，也可以通过索引来取值
# 换句话来说就是集成了列表和字典的特点
print(p[0])
print(p["age"])

print(p[1:])
# 2. 取不连续的行，类似于numpy  如果没有对应的value 则为 Nan
print("="*20)
print(p[[0, 2]])
print(p[["age", "name"]])

"""
    Series 的属性
"""
# .index 取出所有的索引
print(p.index)
print(p.index[1:])
print(len(p.index))
for i in p.index:
    print(i)

# .value 取出所有的值
print(p.values)
print(p.values[:2])

"""
    Series的方法：
        numpy 的很多方法都可以运用于Series类型，比如 argmax，clip
        where方法也有，但有numpy不同
"""
s = pd.Series(range(5))
print(s)
print(s.where(s > 0))  # 小于或等于0 的变成了Nan ，类型自动转化为float

print(s.where(s > 1, 20))  # 将小于等于1 的值变成了 20