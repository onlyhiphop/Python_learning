"""
    数据合并
    join：有返回值, 类似于数据库的join
        默认情况下他是把行索引相同的数据合并到一起
    merge：有返回值
        按照指定的列把数据按照一定的方式合并到一起

    没有的部分会用NaN补充
"""
import pandas as pd
import numpy as np

# join测试
# 具有相同的行索引，不同的列索引
df = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("ABCD"))
print(df)
df2 = pd.DataFrame(np.arange(6).reshape(2, 3), index=list("bc"), columns=list("XYZ"))
print(df2)

# 将df2 join 到 df (会以df为准)
t = df.join(df2)
print(t)

# 将df join到 df2  （会以df2 为准）
t2 = df2.join(df)
print(t2)


# merge测试
"""
    合并方式 
        inner: 交集  (默认的)
        outer : 并集，NaN补全
        left : 左边为准，NaN补全
        right ：右边为准， NaN补全       
"""

t.merge(t2, left_on="A", right_on="Y", how="outer")
