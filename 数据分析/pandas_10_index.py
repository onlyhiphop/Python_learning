"""
    数据索引之复合索引（MultiIndex）
"""
import pandas as pd
import numpy as np

# file_path = "./US_video_data.csv"
# df = pd.read_csv(file_path)
#
# grouped = df.groupby(by=["转发量", "点击量"])
#
# grouped = grouped.count()
#
# print(grouped)
# print(grouped.index)  # MultiIndex

df = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('abc'), columns=list('ABCD'))
print(df)
print(df.index)

# 可以直接通过index属性修改索引
df.index = ["A", "B", "C"]
print(df.index)

# .reindex() 有返回值   不存在D行，所以全为NaN
df2 = df.reindex(["A", "D"])
print(df2)

# .set_index(列, drop=False)  指定某一列作为index
# drop 默认是True ：是否将该列删除
df3 = df.set_index("A", drop=False)
df4 = df.set_index("A", drop=True)
print(df3)
print(df4)

# unique函数去除其中重复的元素，并按元素由大到小返回一个新的无元素重复的元组或者列表
# .index.unique() 返回index的唯一值
print("="*10)
print(df)
print(df["A"])
print(df["A"].unique())
print(type(df["A"].unique()))

print("+"*50)
df.index = ["a", "b", "c"]
df.loc[:, "A"] = "one"
df.loc[:, "B"] = ["o", "p", "q"]
print(df)
df = df.set_index(["A", "B"])
print(df)
#         C   D
# A   B
# one o   2   3
#     p   6   7
#     q  10  11

# 取2这个值
print(df.loc["one"].loc["o"]["C"])

# .swaplevel() ： 复合索引时，要取里面的那层的索引，可以用次方法 交换位置
# 可将第一层索引于第二层索引交换位置
print(df.swaplevel())
print(df.swaplevel().loc["o"])