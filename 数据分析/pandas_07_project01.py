"""
    字符串离散化：
        构造全为0的数组,列名为具体的某项爱好，如果某一条数据中爱好出现过，就让0变成1


"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file_path = "./Test01.csv"

df = pd.read_csv(file_path)
# print(df)

# df["like"].str.split("/") 返回的是Series对象， tolist() 转化成list对象
like_list = df["like"].str.split("/").tolist()
print(like_list)  # 双重list嵌套
# set() 将列表变成set集合（无序不重复）， 可以去掉里面重复的元素, 是用 {} 括起来的
like_set = list(set([j for i in like_list for j in i]))
print(like_set)

# 构造全为0的数组(与数据的行对应)， 列为set中的项
zero_df = pd.DataFrame(np.zeros((df.shape[0], len(like_set))), columns=like_set)
print(zero_df)

# 给每个人出现的like的位置赋值1
# 1. 循环了多次 效率不高 （以行来循环修改）
# for i in range(df.shape[0]):
#     zero_df.loc[i, like_list[i]] = 1

# 2. 循环次数少，效率高 （以列来循环修改）
for ls in like_set:
    # print(df["like"].str.contains(ls))
    zero_df[ls][df["like"].str.contains(ls)] = 1

print(zero_df)

# 统计每个like类型的的和
like_count = zero_df.sum(axis=0)   # 往0轴方向上求和（也就是求每一列的和）
print("="*20)
print(like_count)
print(type(like_count))

# 排序  默认升序 ascending=True
like_count = like_count.sort_values()
print(like_count)
print(type(like_count))   # <class 'pandas.core.series.Series'>

# 画图 ，适合于条形图

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 画条形图
_x = like_count.index
_y = like_count.values
plt.bar(range(len(_x)), _y)  # xy一一对应

# 调整x轴的精度   用整数去一一对应值，再替换
plt.xticks(range(len(_x)), _x)

plt.show()