"""
    数据分组(groupby)和聚合
"""
import pandas as pd
import numpy as np

file_path = "./US_video_data.csv"
df = pd.read_csv(file_path)

# groupby: 按照某个字段分组，相同的为一组
grouped = df.groupby(by="转发量")
print(grouped)   #  DataFrameGroupBy 对象

# DataFrameGroupBy 对象 可以遍历
# DataFrameGroupBy中的每一个元素是一个元组，元组里面是（索引（分组的值）），分组之后的DataFrame
for i, j in grouped:  # grouped中存着两个元组为一项，所以用两个变量取出
    print(i)
    print("-"*20)
    print(j)
    print("=" * 20)

# 需要调用聚合方法
"""
    .count() : 分组中非NA值的数量
    .sum() : 非NA值的和
    .mean() : 非NA值的平均值
    .median() ：非NA值的算术中位数
    .std() .var() 无偏（分母为n-1）标准差和方差
    .min() .max() 非NA值的最小值和最大值
"""
print(grouped["点击量"].count())
print("-"*30)

"""
    数据按照多个条件进行分组， by 参数可以为列表
     下面因为先取了 "转发量" 这一列 它没有 "点击量" "播放量" 字段 所以要加 df
"""
grouped = df["转发量"].groupby(by=[df["点击量"], df["播放量"]]).count()
print(grouped, type(grouped))  # Series

grouped = df[["转发量"]].groupby(by=[df["点击量"], df["播放量"]]).count()
print(grouped, type(grouped))  # DataFrame

# 注意：以上是取法不同，所以分组后的类型也不同
# df["转发量"] 是 Series类型
# df[["转发量"]] 是 DataFrame类型

