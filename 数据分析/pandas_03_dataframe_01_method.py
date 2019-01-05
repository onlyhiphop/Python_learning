"""
    2. DataFrame 二维，Series容器
      类似于数学里面的坐标系
      也相当于Series的集合
"""
import pandas as pd
import numpy as np

"""
    创建 DataFrame对象， 参数可以是 numpy ,dict, DataFrame
"""
# 参数为 ndarray , 不指定0轴和1轴的索引，默认就是 从0开始的索引
df = pd.DataFrame(np.arange(12).reshape(3, 4))
print(df)

# 可以直接指定 0轴和1轴的索引值
df = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("ABCD"))
print(df)

# 参数为字典，自动将key作为1轴（也就是列）
# 如果里面有列表，则会遍历列表取出每一项作为一个字段
persons_dic = {
    "name": ["zhangsan", "lisi", "wangwu"],
    "age": [18, 19, 20],
    "tel": ["1000", "2000", "3000"]
}
infor = pd.DataFrame(persons_dic)
print(infor)

# 参数是列表（列表中字典中的字段不对应，有残缺）
# 对于有的缺的字段， 会自动补充为 NaN
person_list = [
    {"age": 18, "name": "zhangsan"},
    {"name": "lisi", "age": 19},
    {"name": "wangwu", "tel": "1000"},
]
infor2 = pd.DataFrame(person_list)
print(infor2)

"""
    DataFrame的相关属性
    .index  :能得到0轴的所有索引
    .columns : 得到1轴的所有索引
    .values : 得到所有值
    .shape : 得到形状的描述
    .dtypes : 返回每个key的类型
"""
print(infor2.info())
print(infor2.dtypes)
print(infor2.shape)   # (3, 3)

"""
    DataFrame的相关方法
    .head(行数) : 不写默认为前五行
    .tail(行数) ： 得到最后几行
    .info()  : 展示DataFrame对象的信息，概览
    .describe() :能得到一些快速统计的数据信息（标准差，最大，最小，中位数）
    .sort_values(by="按哪个字段排序", ascending=False)  默认升序 ，False为降序
    .mean() 计算平均值 NaN不算进去
    .unique() 返回一个列表   info["age"].unique() 将age列所有的值放进一个列表中返回
"""
print(infor2.describe())
print(infor.sort_values(by="age", ascending=False))

"""
    DataFrame的索引取值操作
    - 方括号写数组，表示取行，对行进行操作
    - 方括号写字符串，表示取列索引，对列进行操作
"""
# 取行
print(infor[:3])  # 取前三行
# 取出 age列 返回 Series对象， 再根据[]里面的条件 选择
print(infor["age"][infor["age"] > 18])
# print(infor[2])  错误的写法

# 取列
print(infor["age"])  # 取 age 这一列  返回的是Series类型
print(infor[["age"]])  # 去age这一类，但返回的是DataFrame

# 联合使用
print("+"*20)
print(infor[:1]["age"])

"""
    DataFrame的选择方式：（和numpy取值一样）
        df.loc  ：通过标签索引行数据 (就是通过DataFrame的0轴和1轴上的索引值)
        df.iloc ：通过位置获取列数据 （通过位置 0... 的索引方式取值）
        
    注意：也能这样进行赋值
            在DataFrame中可以直接赋值np.nan 不需要先转换为float 它会自动转化
"""
"""
    .loc
"""
lc = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("ABCD"))
print(lc)
print("="*20)
# 取 a 行 B 列
print(lc.loc["a", "B"])
# 取 a 行 冒号可以省略
print(lc.loc["a", :])
# 取 C 列
print(lc.loc[:, "C"])
# 去不连续的多行  a 行和 c 行
print(lc.loc[["a", "c"], :])
# 取 a 行 和 c行 的 A列 和C列
print(lc.loc[["a", "c"], ["A", "C"]])
print("="*30)
# 去第a行开始的每一行 的每一列
print(lc.loc["a":, :])
"""
    .iloc
"""
print("-"*20)
# 取第一行的第二列 (a 行 B 列)
print(lc.iloc[0, 1])
# 取第一行和第3行 的第一列和第三列 （a 行 和 c行 的 A列 和C列）
print(lc.iloc[[0, 2], [0, 2]])
# 取第2行开始的每一行的每一列
print(lc.iloc[1:, :])