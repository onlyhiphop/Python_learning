"""
    缺失数据的处理:
        我们的数据缺失通常有两种情况：
            一种是空，Nono等，在pandas是NaN （和np.nan一样）
            另一种是我们让其为 0

    在pandas中判断数据是否为NaN： pd.isnull(df) 如果是NaN 的元素返回是True ，否则是False
                                pd.notnull(df)  刚好和isnunll相反
"""
import pandas as pd
import numpy as np

a = np.arange(12).reshape(3, 4).astype("float")
a[1:, [0, 1]] = np.nan
print(a)
print("="*20)
df = pd.DataFrame(a, index=list("abc"), columns=list("ABCD"))
print(df)
print("="*20)
# df中取出第 A 列不为NaN的元素的所有行
print(df[pd.notnull(df["A"])])

# 1. 删除NaN所在的行列
# .dropna(axis=0, how="any", inplace="False")
#  how 默认参数是 any 只要行中存在NaN就把哪一行删除
#  inplace 默认是False  是否在原来的变量修改，如果是True 就没有返回值，在原来的基础上修改
print(df.dropna(axis=0))
# 参数为 all ，要这一行全为NaN才删除
print(df.dropna(axis=0, how="all"))

# 2. 填充数据  .fillna() 有返回值
print("-"*20)
# 将NaN的元素填充为 100
print(df)
print(df.fillna(100))
#  .mean() 求每一列的均值（如果有NaN，则不加入进行平均运算）
# 对每一列进行取均值
print(df.mean())
# 对指定的列进行取均值
print(df["B"].mean())
# .fillna() 和 .mean() 联合使用：将NaN的值变成平均值
df["B"] = df["B"].fillna(df["B"].mean())
print(df)
