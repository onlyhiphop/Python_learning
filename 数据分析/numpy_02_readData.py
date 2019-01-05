"""
    轴（axis）:
        对于一个一维数组只有一个0轴，对于二维数组有 0轴和1轴  三维：0 , 1 ,2 轴

    有了轴的概念之后，我们计算会更加方便，比如计算一个2维数组的平均值，
    必须指定是计算哪个方向上面的数字的平均值
"""
"""
    numpy 读取数据：
    np.loadtxt(frame=            # 文件 ，字符串或产生器，可以是.gz或bz2压缩文件
               dtype=np.float,   # 以什么数据类型读入数组中，默认np.float
               delimiter=None,  # 分隔字符串，默认是任何空格，
               skiprows=0,   # 跳过前 x 行，一般跳过第一行表头
               usecols=None,  # 读取指定的列，索引，元组类型
               unpack=False   # 默认是False，有多少条数据 就有多少行  如果是True 相当于把矩阵转置（行变成列列变成行，对角线翻转）
               )
"""

import numpy as np


file_path = "./US_video_data.csv"

t2 = np.loadtxt(fname=file_path, delimiter=",", dtype="int")

# print(t2)

"""
    1. numpy索引取值
"""
# 索引取行   索引从0开始
# print(t2[2])   # ==> print(t2[2, :])  第一个放行，第二个放列
# # 取多行，和列表的取法一样
# print(t2[2:])
# # 取不连续的多行
# print(t2[[2, 4, 8]])  # ==> t2[[2, 4, 8], :]
#
# # 取列  索引从0开始
# print(t2[:, 1])
# # 取连续的多列
# print(t2[:, 2:])
# # 取不连续的多列
# print(t2[:, [0, 1]])
#
# # 联合定位取出数组中某个值
# # 取出3行4列的值
# a = t2[2, 3]
# print(a)
# print(type(a))

# 取出里面的一部分： 取第三行到第五行，第2列到第4列的值
# print(t2[2:5, 1:4])
#
# # 取多个不相邻的点 ：
# print(t2[[0, 1, 2], [0, 1, 2]])


"""
    2. numpy中数值的修改
"""
num = np.arange(24).reshape((3, 8))

# 当num中大于10的值会变成 False 小于10的会变成True
d = num < 10
print(d)

# 把num中小于10的数都变成 0
num[num < 10] = 0
print(num)

# 取出num中全部大于10的数
d = num[num > 10]
print(d)

# 三元运算符
# python中
a = 3 if 3 > 2 else 4    # 如果 3 > 2 a就取3 否则就取4

# 在numpy中: .where(条件, 真, 假) 注意有返回值
b = np.where(num > 10, 1, 0)
print(b)

# .clip() 裁剪  把小于10的变成10 ， 把大于18的变成18
num = num.clip(10, 18)
print(num)
